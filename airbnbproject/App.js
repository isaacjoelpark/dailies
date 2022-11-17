import React from "react"
import Card from "./Components/Card"
import Main from "./Components/Main"
import Navbar from "./Components/Navbar"

// we are export from this file to the main index.js
export default function App(){
    return(
        <div className="container">
            <Main />
            <Navbar />
            <Card 
            img = ".images/katies-zaferes.png "
            rating = "5.0"
            reviewCount= {6}
            country = "USA"
            title = "Life lessons with Katies Zaferes"
            price = {136}
            />
            <Card 
            img = "./images/fluffykins.png"
            name = "fluffy"
            phone = "(323) 248- 1284"
            />


        </div>
    )
}