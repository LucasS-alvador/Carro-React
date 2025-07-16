import Link from 'next/link'

export default function Menu() {
  return <nav className="flex justify-start gap-10 mb-5 bg-black text-white p-1 ">
      <Link href="/">Home</Link> |
      <Link href="/carro">Carros</Link> |
      <Link href="/carro/incluir">Incluir Carro</Link>
  </nav>
  }