import React, { useEffect, useState } from 'react';

export default function DataRenderer(props) {
  const [state, setState] = useState({})
  const [loading, setLoading] = useState(true)

  useEffect(() => {
      fetch(`/api/${props.dataPath}`).then(res =>
        res.json())
      .then(res => {
          setState(res)
          setLoading(false)
        }
      )
  }, [props.title, props.dataPath])

  return (
    <React.Fragment>
      <main style={{ padding: "1rem 0" }}>
        <h2>{props.title}</h2>
      </main>

      {loading ? "Loading data..." : ""}
      <ul>
        {
          Object.keys(state).map((key,i)=>{
            return (
                <li key={i}><strong>{key}</strong>: {JSON.stringify(state[key])}</li>
              )
          })
        }
      </ul>
    </React.Fragment>
  );
}
