<h1>Grafos</h1>
<p>Implementação da representação dos vários tipos de grafos em Python</p>
<h2>Conteúdo</h2>
<ul>
	<li>Nós
		<ul>
			<li>Simples</li>
			<li>Valorados</li>
		</ul>
	</li>
	<li>Arestas
		<ul>
			<li>Simples</li>
			<li>Valoradas</li>
		</ul>
	</li>
	<li>Grafos
		<ul>
			<li>Simples</li>
			<li>Direcional</li>
		</ul>
	</li>
</ul>
<h3>Nós</h3>
<h4>Classes</h4>
<ul>
	<li>
		<label><b>Nó simples</b></label>
		<p>
			A classe implementada para os nós simples está implementada no arquivo "<b>No.py</b>". <br>
			Ela possui apenas o atributo <i>identificador</i> e um método para retornar o nó como string. <br />
			Por exmplo se possuirmos um nó no qual <i>identificador</i> = <b>1</b>, sua string ficará será "[1]"
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Nó valorado</b></label>
		<p>A classe implementada para os nós valorados está implementada no arquivo "<b>No.py</b>". <br>
		Ela é uma extensão da classe "<b>No</b>"" citada a cima com o acréscimo do atributo <i>valor</i>. <br>
		O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>. <br />
		Por exmplo se possuirmos um nó no qual <i>identificador</i> = <b>1</b> e <i>valor</i> = <b>15</b>, sua string ficará será "[1] {15}"
	</li>
</ul>
