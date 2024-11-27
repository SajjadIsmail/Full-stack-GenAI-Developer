import Image from 'next/image'
import Link from 'next/link'
import ProductCard from './components/ProductCard'
import { error } from 'console'

export default function Home() {
  //throw new Error('!Not today')
  return (
   <main>
    <h1>Hello World</h1>
    <Link href='/Users'>Users</Link>
    <ProductCard />
   </main>
  )
}