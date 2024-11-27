export default function ProductDetails({params,}:{params: {productId:string};}) { 
    return <h1>Dynamic Page {params.productId}</h1>
}