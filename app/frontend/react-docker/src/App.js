import logo from './logo.svg';
import './App.css';
import {LoginForm} from './elements/LoginForm.js';
import {LoginButton} from './elements/LoginButton.js';
import {SigninButton} from './elements/SigninButton.js';

function App() {
  return (
    <div className="App">
      <div className="front-page-headband">
        <LoginButton/>
        <SigninButton/>
      </div>
      <header className="App-header">
        <h1>
          Eldenring Build Creator
        </h1>
        <p>
            Welcome on the front Page of this Elden Ring build simulator
        </p>
      </header>
      <LoginForm/>
    </div>
  );
}

export default App;
