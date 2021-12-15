import React, { useCallback, useEffect, useState } from "react";

// iris-grid is used to display Deephaven tables.
import {
  IrisGrid,
  IrisGridModel,
  IrisGridModelFactory,
} from "@deephaven/iris-grid";

// Import the shim to use the JS API
import dh from "@deephaven/jsapi-shim";

import "./App.scss";

/**
 * A simple React App that displays a Deephaven table in an IrisGrid using the @deephaven/iris-grid package.
 * If the query param `tableName` is provided, it will attempt to open and display that table, expecting it to be present on the server.
 * E.g. http://localhost:3000?tableName=myTable will attempt to open a table `myTable`
 * If no query param is provided, it will attempt to open a new session and create a basic time table and display that.
 */
function App() {
  const [model, setModel] = useState<IrisGridModel>();
  const [message, setMessage] = useState("");

  const initApp = useCallback(async () => {
    try {
      // Connect to the Web API server. By default we just use the same location this server is hosted on.
      // There is a proxy to redirect all traffic from our server to localhost:10000 defined in package.json by default.
      // Change the proxy there if you wish to connect to a different address.
      // https://create-react-app.dev/docs/proxying-api-requests-in-development/

      const baseUrl = new URL("", `${window.location}`);

      const websocketUrl = `${baseUrl.protocol}//${baseUrl.host}`;

      setMessage(`Starting connection...`);
      const connection = new dh.IdeConnection(websocketUrl);

      const types = await connection.getConsoleTypes();

      console.log("Available types:", types);

      // Start a code session. For this example, we use python
      setMessage(`Starting session...`);
      const session = await connection.startSession("python");

      const searchParams = new URLSearchParams(window.location.search);
      const tableName = searchParams.get("tableName");

      if (tableName) {
        // We should try and open the existing table
        setMessage(`Retrieving table ${tableName}...`);

        const definition = { name: tableName, type: dh.VariableType.TABLE };
        const table = await session.getObject(definition);

        setMessage(`Creating model...`);

        const newModel = await IrisGridModelFactory.makeModel(table);

        setModel(newModel);
      } else {
        // Run code to create a ticking table
        // This table will tick once every second, with a column A indicating the row number
        setMessage(`Creating table...`);
        await session.runCode("from deephaven.TableTools import timeTable");
        const result = await session.runCode(
          't = timeTable("00:00:01").update("A=i")'
        );

        const createdObject = result.changes.created[0];

        setMessage(`Retrieving table ${createdObject.name}...`);

        const table = await session.getObject(createdObject);

        setMessage(`Creating model...`);

        const newModel = await IrisGridModelFactory.makeModel(table);

        setModel(newModel);
      }
    } catch (err) {
      setMessage(`Error: ${err}`);
    }
  }, []);

  useEffect(() => {
    initApp();
  }, [initApp]);

  const isLoaded = model != null;

  return (
    <div className="App">
      {!isLoaded && <div className="message">{message}</div>}
      {isLoaded && <IrisGrid model={model} />}
    </div>
  );
}

export default App;
