import React, { useCallback, useEffect, useState } from 'react';
import { Provider } from 'react-redux';

// iris-grid is used to display Deephaven tables. 
import { Formatter, IrisGrid, IrisGridModel, IrisGridModelFactory } from '@deephaven/iris-grid';
import { DateTimeColumnFormatter } from '@deephaven/iris-grid/dist/formatters';

// Import the shim to use the JS API
import dh from '@deephaven/jsapi-shim';
import { setWorkspace, store } from '@deephaven/redux';

import './App.scss';

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
      // Connect to the Web API server. By default we just use the same location this server is hosted on.
      // There is a proxy to redirect all traffic from our server to localhost:10000 defined in package.json by default.
      // Change the proxy there if you wish to connect to a different address.
      // https://create-react-app.dev/docs/proxying-api-requests-in-development/
      setMessage(`Starting connection...`);
      const connection = new dh.IdeConnection(`${window.location}`);
  
      // Start a code session. For this example, we use python
      setMessage(`Starting session...`);
      const session = await connection.startSession('python');
  
      // Run code to create a ticking table
      // This table will tick once every second, with a column A indicating the row number
      setMessage(`Creating table...`);
      const result = await session.runCode(`
      from deephaven.TableTools import timeTable
      t = timeTable("00:00:01").update("A=i")
      `);
  
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
