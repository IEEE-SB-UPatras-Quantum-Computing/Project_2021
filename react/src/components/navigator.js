import './components.css';
import './navigator.css';

function NavBar(props) {
    function active(algorithm="") {
        return props.algorithm===algorithm?"active":"";
    }

    return (
        <nav id="navigator">
            <a class={"home-link " + active()} href="/" > Home </a>
            <div class="right navMenu">
                <a class={active("superdense")} href="/superdense" > Superdense </a>
                <a class={active("teleportation")} href="/teleportation" > Teleportation </a>
                <a class={active("cryptography")} href="/cryptography" > Quantum Cryptography </a>
                <div class="dot" />
            </div>
        </nav>
    );
}

export default NavBar;
