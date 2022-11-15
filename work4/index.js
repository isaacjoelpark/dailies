ReactDOM.render(<h1>Hello, Everyone!</h1>,document.getElementById("root"))
ReactDom.render(<p>hi, my name is isaac</p>,document.getElementById("root"))
ReactDOM.render(<ul><li>one</li><li>two</li></ul>,document.getElementById("root"))
function Navbar() {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" href="#">Navbar</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                <li className="nav-item active">
                    <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">Link</a>
                </li>
                <li className="nav-item dropdown">
                    <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Dropdown
                    </a>
                    <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a className="dropdown-item" href="#">Action</a>
                    <a className="dropdown-item" href="#">Another action</a>
                    <div className="dropdown-divider"></div>
                    <a className="dropdown-item" href="#">Something else here</a>
                    </div>
                </li>
                <li className="nav-item">
                    <a className="nav-link disabled" href="#">Disabled</a>
                </li>
                </ul>
                <form className="form-inline my-2 my-lg-0">
                    <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" />
                    <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                </form>
            </div>
        </nav>
    )
}
function MainContent(){
    return(
        <h1>I'm learning react!</h1>
    )
}
// ReactDOM.render(
//     <Navbar />,
//     <MainContent />
//     document.getElementById("root")
// )
// const elment = <h1> className = "header"> This is JSX</h1>
// const h1 = document.createElement("h1")
// h1.textContent = "This is an imperative way to program"
// h1.className = "header"
// document.getElementById("root").append(h1)
// ReactDom.render(element, docment.getElementById("root"))

// const page = (
//     <div>
//         <h1 className = "header">This is JSX</h1>
//         <p>This is a paragraph</p>
//     </div>
// )
// ReactDOM.render(page,document.getElementById("root"))
// const plain = (
//     <nav>
//         <h1>ISAAC</h1>
//         <ul>
//             <li>Pricing</li>
//             <li>About</li>
//             <li>Contact</li>
//         </ul>
//     </nav>
// )
// ReactDOM.render(plain, docment.getElementById("root"))
// import React from "react"
// import ReactDom from 'react-dom'

// const page = (
//     <div>
//         <img src='./react-logo.png'width="40px"/> 
        // <div>
        //     <h1>Fun facts about React</h1>
        //     <ul>
        //         <li>Was first released in 2013</li>
        //         <li>was orginally ccreated by Jordan walke</li>
        //         <li>is maintaned by fb</li>
        //         <li>power thousands of enterprise apps, including mobile apps</li>
        //         </ul>
        // </div>
//     </div>
// )

// ReactDom.render(page, document.getElementById("root"))
// function TempName(){
//     return (
//         <div>
//             <h1>Fun facts about React</h1>
//             <ul>
//                 <li>Was first released in 2013</li>
//                 <li>was orginally ccreated by Jordan walke</li>
//                 <li>is maintaned by fb</li>
//                 <li>power thousands of enterprise apps, including mobile apps</li>
//                 </ul>
//         </div>
//     )
// }
// ReactDOM.render(<TempName />, document.getElementById("root"))


import React from "react"
import ReactDOM from "react-dom"
import Header from "./Header"
import Footer from "./Footer"
import MainContent from "./MainContent"

function FunName(){
    return(
        <div>
        <Header />
        <Footer />
        <MainContent />
              </div>
    )
}
ReactDom.render(<FunName />, document.getElementById("root"))