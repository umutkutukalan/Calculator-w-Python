import { useEffect, useState } from "react";
import axios from "axios";

const AllProjects = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    const fetchProjects = async () => {
      const token = localStorage.getItem("token");
      try {
        const response = await axios.get(
          "http://157.230.121.248:8000/Project/getelementbyid/1012",
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
        setProjects(response.data.project);
      } catch (error) {
        console.error("Proje verileri alınamadı", error);
      }
    };

    fetchProjects();
  }, []);

  return (
    <div className="allProjects-height">
      <h1>Projeler</h1>
      <h1> {projects.ProjeAdi} </h1>
    </div>
  );
};

export default AllProjects;
