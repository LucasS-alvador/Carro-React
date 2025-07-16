"use client"
import { useState } from "react";
import styles from "./FormCarro.module.css";

export default function FormCarro() {
  const [form, setForm] = useState({
    modelo: "",
    marca: "",
    ano: "",
    cor: "",
    placa: "",
  });

  function atualizar(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function enviar() {
    fetch("http://localhost:5000/incluir_carro", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    })
      .then(res => res.json())
      .then(res => {
        if (res.resultado === "ok") {
          alert("Carro incluído com sucesso!");
          setForm({
            modelo: "",
            marca: "",
            ano: "",
            cor: "",
            placa: "",
          });
        } else {
          alert("Erro: " + res.detalhes);
        }
      });
  }

  return (
    <div className={styles.container}>
      <h2 className={styles.titulo}>Incluir Carro</h2>

      <div className={styles.formGroup}>
        <label>Modelo</label>
        <input name="modelo" value={form.modelo} onChange={atualizar} />
      </div>

      <div className={styles.formGroup}>
        <label>Marca</label>
        <input name="marca" value={form.marca} onChange={atualizar} />
      </div>

      <div className={styles.formGroup}>
        <label>Ano</label>
        <input name="ano" type="number" value={form.ano} onChange={atualizar} />
      </div>

      <div className={styles.formGroup}>
        <label>Cor</label>
        <input name="cor" value={form.cor} onChange={atualizar} />
      </div>

      <div className={styles.formGroup}>
        <label>Placa</label>
        <input name="placa" value={form.placa} onChange={atualizar} />
      </div>

      <button className={styles.button} onClick={enviar}>Enviar</button>
    </div>
  );
}
