// import React from "react"
// import ReactDOM form "react-dom"
// import App from "./App"

// ReactDOM.render(<App />,document.getElementById("root"))
import React from "react"
export default function App(){
    const [count, setCount] = React.useState(0)
}
    function subtract(){
        setCount(prevCount => prevcount - 1)
    }

    function addition(){
        setCount(prevCount => prevCount + 1)
    }
    return(
        <div className="counter">
            <button className="counter--minus" onClick={subtract}>-</button>
            <div className="counter-count">
                <h1>{count}</h1>
            </div>
            <button className="counter--plus" onClick={addition}>+</button>
        </div>
    )
