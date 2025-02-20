import React from 'react';
import '../static/styles/quantumAlgorithmStyle.scss';

const host = 'http://localhost:5000';

interface QuantumAlgProps {
    name: string;
    algorithm: string;
    properties: string[];
}

function QuantumAlg(props: QuantumAlgProps) {
    //fetch("${host}?q_num=2");
    //const xhr = new XMLHttpRequest()
    //xhr.open("GET", "${host}?q_num=2")
    return (
        <section className='algorithm'>
            <div className="title">
                THIS IS THE QUANTUM ALGORITHM: <br />QUANTUM {props.name}!
            </div>
            <section className="algorithm-body">
                <aside className="helper">
                    <a href={`${host}?algorithm=${props.algorithm}&q_num=2`}>2 QUBITS</a> <br />
                    <a href={`${host}?algorithm=${props.algorithm}&q_num=3`}>3 QUBITS</a> <br />
                    <a href={`${host}?algorithm=${props.algorithm}&q_num=4`}>4 QUBITS</a> <br />
                    <div className="info">
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus aliquam ipsam debitis facere, ex commodi assumenda. Libero fuga dicta fugiat modi blanditiis natus qui, voluptas id earum porro est doloremque aut eum. Molestias illo distinctio error laudantium vero porro provident recusandae, eligendi nisi, quo saepe laborum! Atque in voluptas officia!
                        </p>
                    </div>
                    <form className="properties" method="get"> {/*action={`${host}`}*/}
                        {props.properties.map( (prop: any) => {
                            return (
                                <div className="property">
                                    <label htmlFor={prop}>{prop}</label>
                                    <input id={prop} name={prop} />
                                </div>
                            );})
                        }
                        <input type="submit" />
                    </form>
                </aside>
                <main>
                    {['circ.jpg', 'qsphere.jpg', 'qubits.jpg', 'hist.jpg'].map( filename => {
                        return (<img src={"static/"+props.algorithm+"/"+filename} alt='circuit' width="50%" draggable="false" />);
                    })}
                    <div>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        Officiis quibusdam laborum neque est quam numquam cupiditate illum explicabo,
                        dolore sit soluta fuga nesciunt ullam? Repudiandae iusto ipsam nostrum eaque,
                        suscipit asperiores recusandae dolor illo provident totam reprehenderit,
                        omnis eos cumque nam officia nesciunt quo laudantium temporibus, sunt aliquid quia consequuntur facilis labore porro?
                        Pariatur molestias aspernatur dolor quis a voluptatibus aperiam laudantium impedit voluptates libero, consectetur nobis eos.
                        Recusandae ipsa molestiae assumenda, accusamus ipsam optio libero ad iste quas quo impedit doloremque nam possimus fugit asperiores voluptas aperiam quibusdam incidunt laudantium!
                        Quia, nobis? Aspernatur mollitia vel explicabo aliquid fugit maxime!
                    </div>
                </main>
            </section>
        </section>
    );
}

export default QuantumAlg;
