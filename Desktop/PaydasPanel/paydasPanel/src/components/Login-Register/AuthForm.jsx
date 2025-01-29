import { useState } from "react";
import axios from "axios";
import { authformImg } from "../utils";

const AuthForm = ({ setIsAuthenticated }) => {
  const [isRegistering, setIsRegistering] = useState(false);
  const [ad, setAd] = useState("");
  const [soyad, setSoyad] = useState("");
  const [mail, setMail] = useState("");
  const [sifre, setSifre] = useState("");
  const [telefon, setTelefon] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://157.230.121.248:8000/Session/login",
        {
          Mail: mail,
          Sifre: sifre,
        }
      );
      const token = response.data.token;
      localStorage.setItem("token", token);
      setIsAuthenticated(true);
      resetForm();
    } catch (error) {
      alert("Geçersiz kullanıcı adı veya şifre", error);
    }
  };

  const resetForm = () => {
    setAd("");
    setSoyad("");
    setMail("");
    setSifre("");
    setTelefon("");
  };

  return (
    <div className="authform-height flex-center">
      <div className="authform-table">
        <div className="authform-table-content flex-1">
          <div className="w-full flex flex-col gap-4 px-15">
            <div>
              <h1 className="font-orbitron text-3xl">BIMESIS</h1>
              <h3>Anlık takip, paydas panel!</h3>
            </div>
            <div>
              <div className="w-full border-b border-gray-300"></div>
            </div>
            <form onSubmit={handleSubmit} className="flex flex-col gap-5">
              {isRegistering ? (
                <div className="flex flex-col gap-4">
                  <div className="flex items-center gap-4">
                    <div className="authform-row">
                      <input
                        type="text"
                        placeholder="Ad"
                        value={ad}
                        className="authform-input"
                        onChange={(e) => setAd(e.target.value)}
                      />
                    </div>
                    <div className="authform-row">
                      <input
                        type="text"
                        placeholder="Soyad"
                        value={soyad}
                        className="authform-input"
                        onChange={(e) => setSoyad(e.target.value)}
                      />
                    </div>
                  </div>
                  <div className="authform-row">
                    <input
                      type="text"
                      placeholder="Telefon"
                      value={telefon}
                      className="authform-input"
                      onChange={(e) => setTelefon(e.target.value)}
                    />
                  </div>
                </div>
              ) : (
                ""
              )}
              <div className="authform-row">
                <input
                  type="text"
                  placeholder="Email"
                  value={mail}
                  className="authform-input"
                  onChange={(e) => setMail(e.target.value)}
                />
              </div>
              <div className="authform-row">
                <input
                  type="password"
                  placeholder="Sifre"
                  value={sifre}
                  className="authform-input"
                  onChange={(e) => setSifre(e.target.value)}
                />
              </div>
              <button type="submit" className="authform-btn">
                {isRegistering ? "Kaydol" : "Giriş Yap"}
              </button>
            </form>
            <div className="flex items-center gap-1 text-xs flex-center">
              <p className="text-gray-500">
                {isRegistering
                  ? "Zaten hesabınız var mı?"
                  : "Henüz hesabınız yok mu?"}
              </p>
              <a
                href="#"
                className="font-semibold underline"
                onClick={() => {
                  setIsRegistering(!isRegistering);
                  resetForm();
                }}
              >
                {isRegistering ? "Giriş Yap" : "Kaydol"}
              </a>
            </div>
          </div>
        </div>
        <div className="authform-table-image flex-1">
          <img
            src={authformImg}
            alt=""
            className="h-full w-full object-cover rounded-r-3xl"
          />
        </div>
      </div>
    </div>
  );
};

export default AuthForm;
