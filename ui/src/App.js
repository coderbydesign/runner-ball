import { Outlet, Link } from "react-router-dom";

function App() {
  return (
    <div>
      <h1>Runner Ball</h1>
      <nav
        style={{
          borderBottom: "solid 1px",
          paddingBottom: "1rem",
        }}
      >
        <Link to="/weather">Weather</Link> |{" "}
        <Link to="/score">Score</Link> |{" "}
        <Link to="/bulb">Bulb</Link>
      </nav>
      <Outlet />
    </div>
  );
}

export default App;
