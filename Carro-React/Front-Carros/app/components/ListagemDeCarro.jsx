"use client"
import { useEffect, useState } from "react";
import styles from "./ListagemDeCarros.module.css";

export default function ListagemDeCarros() {
  const [carros, setCarros] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/listar_carros")
      .then(res => res.json())
      .then(res => {
        if (res.resultado === "ok") {
          setCarros(res.detalhes);
        }
      });
  }, []);

  return (
    <div className={styles.container}>
      <h2 className={styles.titulo}>Lista de Carros</h2>
      <ul className={styles.lista}>
        {carros.map((carro, index) => (
          <li key={index} className={styles.item}>
            <span><strong>Modelo:</strong> {carro.modelo}</span><br />
            <span><strong>Marca:</strong> {carro.marca}</span><br />
            <span><strong>Ano:</strong> {carro.ano}</span><br />
            <span><strong>Cor:</strong> {carro.cor}</span><br />
            <span><strong>Placa:</strong> {carro.placa}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
