class Proper extends React.Component {
    constructor() {
        super();
        this.meter = {
            value: 0
        };
        this.state = {
            meter: 1,
            millimeter: 1000
        };
    }


    meterToMillimeter(meter) {
        // document.getElementById('result').style.display = 'block';
        this.setState({
            meter: meter.target.value,
            millimeter: meter.target.value * 1000
        });
    }

    millimeterToMeter(millimeter) {
        // document.getElementById('result').style.display = 'block';
        this.setState({
            meter: millimeter.target.value / 1000,
            millimeter: millimeter.target.value
        });
    }

    render() {
        // return this.htmlCode;
        return (
            <div id="body-wrapper">
                <div id="head-wrapper">
                    <h3>Amount</h3>
                    <hr/>
                </div>

                <div id="center-wrapper">
                    <table>
                        <tr>
                            <td><span className="word">From</span></td>
                            <td colSpan="2"><span className="word">To</span></td>
                        </tr>
                        <tr>
                            <td>
                                <input type="text" name={"meter"} value={this.state.meter} placeholder={"1"} required
                                       onChange={this.meterToMillimeter.bind(this)}
                                />
                            </td>
                            <td>
                                <input type="text" name={"millimeter"} value={this.state.millimeter} required
                                       onChange={this.millimeterToMeter.bind(this)}
                                />
                            </td>
                            <td>
                                <button id="btn-convert" className={"btn"}
                                    // onClick={this.meterToMillimeter(document.getElementById('meter'))}
                                >
                                    CONVERT
                                </button>
                            </td>
                        </tr>
                    </table>
                </div>
                {/*<br/>*/}
                <div id="footer-wrapper">
                    <p id="result" className={"result word"}>
                        <span className="result-num">{this.state.meter}</span>m is <span
                        className="result-num">{this.state.millimeter}</span>mm.
                    </p>
                </div>
            </div>
        )
    }
}

ReactDOM.render(
    <Proper/>,
    document.getElementById('wrapper')
)
