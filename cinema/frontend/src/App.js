import "./App.css";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Cookies from "universal-cookie";
import UserList from "./components/UserList/UserList";
import CinemaList from "./components/CinemaList/CinemaList";
import LoginForm from "./components/Auth.js";

function App() {
  const set_token = (token) => {
    const cookies = new Cookies();
    cookies.set("bearer", token);
    setState({ token: token}, () => load_data() );
  };
  const is_authenticated = () => {
    return state.token != "";
  };
  const logout = () => {
    set_token("");
  };
  const get_token_from_storage = () => {
    const cookies = new Cookies();
    const token = cookies.get("bearer");
    setState({ token: token }, ()=>load_data());
  };
  const get_headers = () => {
    let headers = {
    'Content-Type': 'application/json'
    }
    if (this.is_authenticated())
    {
    headers['Authorization'] = 'Bearer ' + token
    }
    return headers
    }
    
  const get_token = (username, password) => {
    axios
      .post("http://127.0.0.1:8000/api/token", {
        username: username,
        password: password,
      })
      .then((response) => {
        set_token(response.data["token"]);
      })
      .catch((error) => alert("Неверный логин или пароль"));
  };

  const load_data = () => {
    axios
      .get("http://127.0.0.1:8000/api/users/")
      .then((response) => {
        this.setState({ authors: response.data });
      })
      .catch((error) => console.log(error));
    axios
      .get("http://127.0.0.1:8000/api/cinema/")
      .then((response) => {
        this.setState({ books: response.data });
      })
      .catch((error) => console.log(error));
  };

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
          <li>
            <Link to="/login">Login</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<UserList />} />
        <Route path="/cinema" element={<CinemaList />} />
        <Route
          path="/login"
          element={
            <LoginForm
              get_token={(username, password) => get_token(username, password)}
            />
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
