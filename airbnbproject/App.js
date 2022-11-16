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
            <Card />
        </div>
    )
}