import React, { Component } from 'react'


class Card extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div className="vert">
               <h4>{this.props.elem.name}</h4>
               <br/> 

               <h5>Price: ${this.props.elem.price.toFixed(2)}</h5>             
                <button className="btn" 
                name={this.props.elem.group} 
                form={this.props.elem.name}
                value={this.props.elem.price.toFixed(2)} 
                onClick={this.props.handleClick} >Add</button>
                <button className="btn" name={this.props.elem.group} onClick={this.props.handleRemove}>Remove Last Item</button>
                <button className="btn" name={this.props.elem.group} onClick={this.props.handleNext}>Next</button>
            </div>
        )
    }
}


export default Card

