import React, { useCallback, useEffect, useState } from "react";
import { LoadingOverlay } from "@deephaven/components"; // Use the loading spinner from the Deephaven components package
import {
  IrisGrid,
  IrisGridModel,
  IrisGridModelFactory,
} from "@deephaven/iris-grid"; // iris-grid is used to display Deephaven tables
import dh from "@deephaven/jsapi-shim"; // Import the shim to use the JS API
import "./App.scss"; // Styles for in this app

/**
 * Load an existing Deephaven table with the session provided
 * @param session The Deephaven session object
 * @param name Name of the table to load
 * @returns Deephaven table
 */
async function loadTable(session: any, name: string) {
  console.log(`Fetching table ${name}...`);

  const definition = { name, type: dh.VariableType.TABLE };
  return session.getObject(definition);
}

/**
 * Create a new Deephaven table with the session provided.
 * Creates a table that will tick once every second, with two columns:
 * - Timestamp: The timestamp of the tick
 * - A: The row number
 * @param session The Deephaven session object
 * @param name Name of the table to load
 * @returns Deephaven table
 */
async function createTable(session: any) {
  console.log(`Creating table...`);

  await session.runCode("from deephaven.TableTools import timeTable");
  const result = await session.runCode(
    't = timeTable("00:00:01").update("A=i")'
  );

  const definition = result.changes.created[0];

  console.log(`Fetching table ${definition.name}...`);

  return await session.getObject(definition);
}

/**
 * A functional React component that displays a Deephaven table in an IrisGrid using the @deephaven/iris-grid package.
 * If the query param `tableName` is provided, it will attempt to open and display that table, expecting it to be present on the server.
 * E.g. http://localhost:3000/?tableName=myTable will attempt to open a table `myTable`
 * If no query param is provided, it will attempt to open a new session and create a basic time table and display that.
 * By default, tries to connect to the server defined in the REACT_APP_CORE_API_URL variable, which is set to http://localhost:1000/jsapi
 * See create-react-app docs for how to update these env vars: https://create-react-app.dev/docs/adding-custom-environment-variables/
 */
function App() {
  const [model, setModel] = useState<IrisGridModel>();
  const [error, setError] = useState<string>();
  const [isLoading, setIsLoading] = useState(true);

  const initApp = useCallback(async () => {
    try {
      // Connect to the Web API server
      const baseUrl = new URL(
        process.env.REACT_APP_CORE_API_URL ?? `${window.location}`
      );

      const websocketUrl = `${baseUrl.protocol}//${baseUrl.host}`;

      console.log(`Starting connection...`);
      const connection = new dh.IdeConnection(websocketUrl);

      // Start a code session. For this example, we use python.
      console.log(`Starting session...`);
      const session = await connection.startSession("python");

      // Get the table name from the query param `tableName`.
      const searchParams = new URLSearchParams(window.location.search);
      const tableName = searchParams.get("tableName");

      // If a table name was specified, load that table. Otherwise, create a new table.
      const table = await (tableName
        ? loadTable(session, tableName)
        : createTable(session));

      // Create the `IrisGridModel` for use with the `IrisGrid` component
      console.log(`Creating model...`);

      const newModel = await IrisGridModelFactory.makeModel(table);

      setModel(newModel);

      console.log("Table successfully loaded!");
    } catch (e) {
      console.error("Unable to load table", e);
      setError(`${e}`);
    }
    setIsLoading(false);
  }, []);

  useEffect(() => {
    initApp();
  }, [initApp]);

  const isLoaded = model != null;

  return (
    <div className="App">
      {isLoaded && <IrisGrid model={model} />}
      {!isLoaded && (
        <LoadingOverlay
          isLoaded={isLoaded}
          isLoading={isLoading}
          errorMessage={error ? error : null}
        />
      )}
    </div>
  );
}

export default App;
