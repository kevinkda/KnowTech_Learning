const VDOM = <h1>Hello, React.</h1>

function meterToMillimeter(meter) {
    return meter * 1000;
}

function formatOutput(meter) {
    return meter + 'm is ' + meterToMillimeter(meter) + 'mm';
}

// //监控文本框的change事件
// numChange = (e) => {
//     console.log(this.refs.txt.value)
//     console.log(e)
//     const newVal = e.target.value
//     this.setState({
//         mydata: newVal
//     })
// }


const htmlCode = (
    <div id="center-wrapper">
        <h3>Amount</h3>
        <hr/>
        <table>
            <tr>
                <td>From</td>
                <td colSpan="2">To</td>
            </tr>
            <tr>
                <td><input type="text" id="input-orginal"/></td>
                <td>
                    {/*<input ref="txt" onChange={(e) => this.numChange(e)} type="text" style={{width: '100%'}}*/}
                    {/*       // id="input-orginal"*/}
                    {/*       value={this.state.mydata}/>*/}
                </td>
                <td>
                    <input type="text" id="input-new"/>
                </td>
                <td>
                    <button id="btn-convert">CONVERT</button>
                </td>
            </tr>
        </table>
        <br/>
        <div>
            <p id="result">{formatOutput(document.getElementById("input-orginal"))}</p>
        </div>
    </div>
)


// let btnConvert;
//     < btnConvert
// color = "blue"
// shadowSize = {2} >
//     CONVERT
//     < /btnConvert>

// ReactDOM.render(VDOM, wrapper);
// ReactDOM.render(VDOM, document.getElementById('wrapper'));
ReactDOM.render(htmlCode, document.getElementById('wrapper'));
// React.createElement(
//     btnConvert
// )
