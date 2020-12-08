import React, { Component } from 'react'

class Header extends Component {
    constructor(props) {
        super(props)

        this.state = {
                 
        }

    }

    render() {
        return (
            <div className="header">
                <div>
                    <h1>Welcome to Philly Crepes!!</h1>

                </div>
               <br/> 
                <div>
                <p>Please select your choice of wrap and 
                   fruit from the menu below:
               </p>   
                </div>
                        
               <br/> 
            </div>
        )
    }
}


export default Header

