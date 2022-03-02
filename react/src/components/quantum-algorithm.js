import './components.css';
import './quantum-algorithm.css';

function QuantumAlg(props) {
    //fetch("http://127.0.0.1:5000?q_num=2");
    //const xhr = new XMLHttpRequest()
    //xhr.open("GET", "http://127.0.0.1:5000?q_num=2")
    return (
        <section class='algorithm'>
            <div class="title">
                THIS IS THE QUANTUM ALGORITHM: <br />
                QUANTUM {props.name}!
            </div>
            <section class="algorithm-body">
                <aside class="helper">
                    <a href={`http://127.0.0.1:5000?algorithm=${props.algorithm}&q_num=2`}>2 QUBITS</a> <br />
                    <a href={`http://127.0.0.1:5000?algorithm=${props.algorithm}&q_num=3`}>3 QUBITS</a> <br />
                    <a href={`http://127.0.0.1:5000?algorithm=${props.algorithm}&q_num=4`}>4 QUBITS</a> <br />
                    <div class="info">
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus aliquam ipsam debitis facere, ex commodi assumenda. Libero fuga dicta fugiat modi blanditiis natus qui, voluptas id earum porro est doloremque aut eum. Molestias illo distinctio error laudantium vero porro provident recusandae, eligendi nisi, quo saepe laborum! Atque in voluptas officia!
                        </p>
                    </div>
                    <form class="properties" method="get"> {/*action={`http://127.0.0.1:5000`}*/}
                        {props.properties.map( prop => {
                            return (
                                <div class="property">
                                    <label for={prop}>{prop}</label>
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
                    {/* <img src='static/circ.jpg' alt='circuit' width="50%" draggable="false" />
                    <div>
                        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eum ad officiis dolores debitis, sint qui quam ipsum. Pariatur eos optio rerum fuga veniam suscipit nihil vero explicabo blanditiis magni, vitae sint perferendis voluptas accusantium iusto, consequatur ex facere consequuntur. Minus est maxime ad. Accusantium hic inventore, et maxime facere quasi maiores doloribus amet veritatis exercitationem cumque ea reprehenderit nostrum rerum ipsa quas in, assumenda ipsam repudiandae magnam!
                    </div>
                    <img src='static/hist.jpg' alt='histogram' width="50%" draggable="false" />
                    <div>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis quibusdam laborum neque est quam numquam cupiditate illum explicabo, dolore sit soluta fuga nesciunt ullam? Repudiandae iusto ipsam nostrum eaque, suscipit asperiores recusandae dolor illo provident totam reprehenderit, omnis eos cumque nam officia nesciunt quo laudantium temporibus, sunt aliquid quia consequuntur facilis labore porro? Pariatur molestias aspernatur dolor quis a voluptatibus aperiam laudantium impedit voluptates libero, consectetur nobis eos. Recusandae ipsa molestiae assumenda, accusamus ipsam optio libero ad iste quas quo impedit doloremque nam possimus fugit asperiores voluptas aperiam quibusdam incidunt laudantium! Quia, nobis? Aspernatur mollitia vel explicabo aliquid fugit maxime!
                    </div>
                    <img src='static/qsphere.jpg' alt='q-sphere' width="50%" draggable="false" />
                    <div>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis quibusdam laborum neque est quam numquam cupiditate illum explicabo, dolore sit soluta fuga nesciunt ullam? Repudiandae iusto ipsam nostrum eaque, suscipit asperiores recusandae dolor illo provident totam reprehenderit, omnis eos cumque nam officia nesciunt quo laudantium temporibus, sunt aliquid quia consequuntur facilis labore porro? Pariatur molestias aspernatur dolor quis a voluptatibus aperiam laudantium impedit voluptates libero, consectetur nobis eos. Recusandae ipsa molestiae assumenda, accusamus ipsam optio libero ad iste quas quo impedit doloremque nam possimus fugit asperiores voluptas aperiam quibusdam incidunt laudantium! Quia, nobis? Aspernatur mollitia vel explicabo aliquid fugit maxime!
                    </div>
                    <img src='static/qubits.jpg' alt='qubits' width="50%" draggable="false" /> */}
                    <div>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis quibusdam laborum neque est quam numquam cupiditate illum explicabo, dolore sit soluta fuga nesciunt ullam? Repudiandae iusto ipsam nostrum eaque, suscipit asperiores recusandae dolor illo provident totam reprehenderit, omnis eos cumque nam officia nesciunt quo laudantium temporibus, sunt aliquid quia consequuntur facilis labore porro? Pariatur molestias aspernatur dolor quis a voluptatibus aperiam laudantium impedit voluptates libero, consectetur nobis eos. Recusandae ipsa molestiae assumenda, accusamus ipsam optio libero ad iste quas quo impedit doloremque nam possimus fugit asperiores voluptas aperiam quibusdam incidunt laudantium! Quia, nobis? Aspernatur mollitia vel explicabo aliquid fugit maxime!
                    </div>
                </main>
            </section>
        </section>
    );
}

export default QuantumAlg;
