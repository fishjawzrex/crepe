import React from "react";
import ReactDOM from "react-dom";
import Card from "./components/card.js";
import Container from "./components/container.js";
import Header from "./components/header.js";
import "./App.css"


 class App extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
         order: [],
         loaded: false,
    }
    this.handleClick = this.handleClick.bind(this)
    this.handleRemove = this.handleRemove.bind(this)
    this.handleNext = this.handleNext.bind(this)
  }

  async componentDidMount() {

    const fruits_resp = await fetch('http://localhost:8000/fruits/')
    const nuts_resp = await fetch('http://localhost:8000/nuts/')
    const toppings_resp = await fetch('http://localhost:8000/toppings/')
    const sides_resp = await fetch('http://localhost:8000/sides/')
    const wraps_resp = await fetch('http://localhost:8000/wraps/')
    const drinks_resp = await fetch('http://localhost:8000/beverages/')
    const fruits_data = await fruits_resp.json()
    const nuts_data = await nuts_resp.json()
    const toppings_data = await toppings_resp.json()
    const sides_data = await sides_resp.json()
    const wraps_data = await wraps_resp.json()
    const drinks_data = await drinks_resp.json()

    this.setState({
      fruit : {name:"fruit", data:fruits_data, limit:2, count:0},                    
      nut : {name:"nut", data:nuts_data, limit:2, count:0}, 
      topping : {name:"topping", data:toppings_data, limit:2, count:0}, 
      side : {name:"side", data:sides_data, limit:2, count:0}, 
      wrap : {name:"wrap", data:wraps_data, limit:1, count:0}, 
      drink : {name:"drink", data:drinks_data, limit:1, count:0}, 
      loaded:true
                    })

    console.log(Object.keys(this.state))
  
  }

  calculateTotal(arr){
    const reducer = (seed,acc)=>seed+acc;
    alert("Your Total is: "+arr.reduce(reducer))
    alert("Thank you for shopping with us!")
    return arr.reduce(reducer)
  }

  handleClick(event){
    const arr = event.target.name

    const work = () => {
      this.setState((prev)=>{prev.order.push((parseFloat(event.target.value)))
      
        this.state[arr].count=prev[arr].count+1
        
       });
     console.log(this.state.fruit.data, this.state.order)
     console.log(this.state[arr], arr)
    }
    {this.state[arr].count==this.state[arr].limit?(event.target.parentElement.parentElement.style.display="none"):work()}
    // {this.state[arr].count==this.state[arr].limit&&(event.target.parentElement.parentElement.style.display="none")}
    {this.state[arr].name=="drink"&&this.calculateTotal(this.state.order)}

    
  }
  handleRemove(event){
    const arr = event.target.name
    const work = ()=>{
      this.setState(prev=>{this.state.order.pop()
        this.prev[arr].count=prev[arr].count-1
      })
      console.log(this.state.order)
    }
    {this.state[arr].count>=0&&work()}

  }

  handleNext(event){
    const arr = event.target.name
    const work = ()=>{
      this.setState(prev=>{this.state.order.pop()
        this.state[arr].count=prev[arr].count-1
      })
      console.log(this.state.order)
    }
    {this.state[arr].count>=0&&work()}

  }

  render() {

    let res = this.state.loaded && [this.state.wrap,this.state.fruit, this.state.nut, this.state.topping, this.state.side, this.state.drink]
    res = Array.from(res)
    return (
      <div >
        {this.state.loaded?<Header/>:<h1>Loading...</h1>}
          <div className="main">
            {res.map(elem=>{
              
              return(
                
                <div >
                  <h1>{elem.name}</h1>
                  {/* <h4>{elem.count}</h4> */}
                  <br/>
                  <p>Please select your choice of {elem.limit} {elem.name}(s) from the menu below:
                  </p> 
                  {elem.data.map(elem => <
                                          Card 
                                          key={elem.id} 
                                          elem={elem} 
                                          handleClick={this.handleClick} 
                                          handleRemove={this.handleRemove} 
                                          handleNext={this.handleNext}
                                          />)}
                </div>
              )
            })}
          </div>
      </div>
    )
  }
}

export default App 