var React = require('react');

var PolyEvent = React.createClass({
  render: function() {
    return (
      <div>
        <Sidebar />
        <div className="pusher">
          <Button />
        </div>
      </div>
    );
  },
});

var Sidebar = React.createClass({
  render: function() {
    return (
      <div className="ui sidebar inverted vertical menu">
        <a className="item">
          1
        </a>
        <a className="item">
          2
        </a>
        <a className="item">
          3
        </a>
      </div>
    )
  }
});

var Button = React.createClass({
  getInitialState: function() {
    return {toggled: false};
  },
  handleClick: function() {
    this.setState({toggled: !this.state.toggled});
    $('.ui.sidebar').sidebar('toggle');
  },
  render: function() {
    var text = this.state.toggled ? 'toggled' : 'untoglled';
    return (
      <div>
        <button onClick={this.handleClick} className="ui primary button">
          {text}
        </button>
      </div>
    );
  },
});

module.exports = PolyEvent;
