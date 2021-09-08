import React, { useCallback, useEffect, useState } from 'react';
import { Provider } from 'react-redux';

// iris-grid is used to display Deephaven tables. 
import { Formatter, IrisGrid, IrisGridModel, IrisGridModelFactory } from '@deephaven/iris-grid';
import { DateTimeColumnFormatter } from '@deephaven/iris-grid/dist/formatters';

// Import the shim to use the JS API
import dh from '@deephaven/jsapi-shim';
import { setWorkspace, store } from '@deephaven/redux';

import './App.scss';

// There is a proxy to redirect all traffic from our server to localhost:10000 defined in package.json by default.
// Change the proxy there if you wish to connect to a different address.
// https://create-react-app.dev/docs/proxying-api-requests-in-development/
const websocketUrl = `${window.location}`;

// For this example, we're using python.
const consoleType = 'python';

// Code to create an empty table
const emptyTableCode = `
from deephaven.TableTools import timeTable
t = timeTable("00:00:02").update("A=i")
`;

// We need to define the workspace so the proper time zone is used in the grid
store.dispatch(setWorkspace({
  data: {
    settings: {
      defaultDateTimeFormat:
        DateTimeColumnFormatter.DEFAULT_DATETIME_FORMAT_STRING,
      formatter: Formatter.getDefaultFormattingRules(),
      timeZone: DateTimeColumnFormatter.DEFAULT_TIME_ZONE_ID,
      showTimeZone: false,
      showTSeparator: true,
      disableMoveConfirmation: false,
    },
  }
}));

function App() {
  const [ model, setModel ] = useState<IrisGridModel>();
  const [ message, setMessage ] = useState('');

  const initApp = useCallback(async () => {
    try {
      setMessage(`Starting connection to ${websocketUrl}...`);
    
      const connection = new dh.IdeConnection(websocketUrl);
  
      setMessage(`Starting session with type ${consoleType}...`);
    
      const session = await connection.startSession(consoleType);
  
      setMessage(`Creating table...`);
  
      const result = await session.runCode(emptyTableCode);
  
      const createdObject = result.changes.created[0];
  
      setMessage(`Retrieving table ${createdObject.name}...`);
  
      const table = await session.getObject(createdObject);
  
      setMessage(`Creating model...`);
  
      const newModel = await IrisGridModelFactory.makeModel(table);
  
      setModel(newModel);
    } catch (err) {
      setMessage(`Error: ${err}`);
    }
  }, []);

  useEffect(() => {
    initApp();
  }, [ initApp]);

  const isLoaded = model != null;

  return (
    <div className="App">
      <Provider store={store}>
        { !isLoaded && <div className="message">{message}</div>}
        { isLoaded && <IrisGrid model={model}/>}
      </Provider>
    </div>
  );
}

export default App;
