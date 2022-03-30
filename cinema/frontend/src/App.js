import "./App.css";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Cookies from "universal-cookie";
import UserList from "./components/UserList/UserList";
import CinemaList from "./components/CinemaList/CinemaList";
import LoginForm from "./components/Auth.js";

function App() {
  return (
    <BrowserRouter>
      <nav>
        <ul class="rounded">
          <li>
            <Link to="/">Users</Link>
          </li>
          <li>
            <Link to="/cinema">Cinema</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<UserList />} />
        <Route path="/cinema" element={<CinemaList />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
