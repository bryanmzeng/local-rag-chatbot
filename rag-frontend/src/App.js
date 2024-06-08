import React, { useState } from 'react';

function App() {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState('');
    const [reset, setReset] = useState(false);
    const [dataDir, setDataDir] = useState('');

    const handleQueryChange = (e) => {
        setQuery(e.target.value);
    };

    const handleDataDirChange = (e) => {
        setDataDir(e.target.value);
    };

    const handleSubmitQuery = async () => {
        try {
            const res = await fetch('http://localhost:5001/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query })
            });
            const data = await res.json();
            setResponse(data.response);
        } catch (error) {
            console.error(error);
            setResponse('Error querying the database.');
        }
    };

    const handleUpdateDatabase = async () => {
        try {
            const res = await fetch('http://localhost:5001/update-database', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ reset })
            });
            const data = await res.json();
            setResponse(data.message);
        } catch (error) {
            console.error(error);
            setResponse('Error updating the database.');
        }
    };

    const handleSetDataDir = async () => {
        try {
            const res = await fetch('http://localhost:5001/set-data-dir', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ data_dir: dataDir })
            });
            const data = await res.json();
            setResponse(data.message);
        } catch (error) {
            console.error(error);
            setResponse('Error setting data directory.');
        }
    };

    return (
        <div className="App">
            <h1>RAG for local files</h1>
            <div>
                <label>
                    Data Directory:
                    <input type="text" value={dataDir} onChange={handleDataDirChange} />
                </label>
                <button onClick={handleSetDataDir}>Set Data Directory</button>
            </div>
            <div>
                <label>
                    Query:
                    <input type="text" value={query} onChange={handleQueryChange} />
                </label>
                <button onClick={handleSubmitQuery}>Submit Query</button>
            </div>
            <div>
                <label>
                    <input
                        type="checkbox"
                        checked={reset}
                        onChange={() => setReset(!reset)}
                    />
                    Reset Database
                </label>
                <button onClick={handleUpdateDatabase}>Update Database</button>
            </div>
            <div>
                <h2>Llama3:</h2>
                <pre>{response}</pre>
            </div>
        </div>
    );
}

export default App;
