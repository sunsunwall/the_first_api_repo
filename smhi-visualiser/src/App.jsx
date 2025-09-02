
import { useEffect, useState } from 'react';
import './App.css';
import { fetchSmhiData } from './smhiData';

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchSmhiData().then((result) => {
      if (result.error) {
        setError(result.error);
      } else {
        setData(result);
      }
    });
  }, []);

  return (
    <div className="App">
      <h1>SMHI Data Visualizer</h1>
      {error && <div style={{ color: 'red' }}>Error: {error}</div>}
      {!data && !error && <div>Loading...</div>}
      {data && (
        <pre style={{ textAlign: 'left', background: '#f4f4f4', padding: '1em', borderRadius: '8px', overflowX: 'auto' }}>
          {JSON.stringify(data, null, 2)}
        </pre>
      )}
      <p style={{ marginTop: '2em', color: '#888' }}>
        Place your <code>smhi_data.json</code> file in the <code>public</code> folder to visualize it here.
      </p>
    </div>
  );
}

export default App;
