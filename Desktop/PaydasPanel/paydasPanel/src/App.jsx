import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";
import AuthForm from "./components/Login-Register/AuthForm";
import AllProjects from "./components/Projeler/AllProjects";
import AllCommissions from "./components/Komisyonlar/AllCommissions";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <Router>
      {isAuthenticated && <Navbar />}
      <div className="app-container">
        {isAuthenticated && <Sidebar />}
        <div className="content-container">
          <Routes>
            {!isAuthenticated ? (
              <Route
                path="/"
                element={<AuthForm setIsAuthenticated={setIsAuthenticated} />}
              />
            ) : (
              <>
                <Route path="/" element={<AllProjects />} />
                <Route path="/about" element={<AllCommissions />} />
              </>
            )}
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
