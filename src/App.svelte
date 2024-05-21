<script>
	import { Button, Col, Row, Offcanvas } from 'sveltestrap/src';
	export let name;
	let isOpen = false;

  const toggle = () => {
    isOpen = !isOpen;
  };
</script>

<Offcanvas header="No Backdrop" {isOpen} {toggle} backdrop={false}>
  Look ma, no backdrop.
</Offcanvas>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<Row>
		<Col>
			<Button color="primary" on:click={toggle}>Open</Button>
		</Col>
	</Row>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>