import React, { Component } from 'react'


class Container extends Component {
    constructor(props) {
        super(props)

        this.state = {
                price: this.props.price 
        }

    }

    render() {
        return (
            <div className="vert">
               <h4>{this.props.data.map(elem=>elem.name)}</h4>
               <br/> 

               {/* <h5>Price: ${this.props.elem.price.toFixed(2)}</h5>             
                <button className="btn" value={this.props.elem.price} onClick={this.props.handleClick} >Add</button>
                <button className="btn">Remove</button> */}
            </div>
        )
    }
}


export default Container

