<script>
  let formData = {
    name: '',
    email: '',
    message: ''
  };

  function handleChange(event) {
    formData = { ...formData, [event.target.name]: event.target.value };
  }

  function handleSubmit(event) {
    event.preventDefault();
    // Aquí puedes manejar el envío del formulario
    console.log(formData);
  }
</script>

<div class="mb-3 page-title">
  <h4>Contacto</h4>
</div>
<hr>
<div class="card border-0">
  <div class="card-header">
    <h5 class="card-title">
      Formulario de Contacto
    </h5>
    <h6 class="card-subtitle text-muted">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum ducimus,
      necessitatibus reprehenderit itaque!
    </h6>
  </div>
  <div class="card-body">
    <div class="row">
      <div class="col-md-6">
        <form on:submit={handleSubmit}>
          <div class="form-group">
            <label for="name">Nombre</label>
            <input
              type="text"
              class="form-control"
              id="name"
              name="name"
              placeholder="Ingrese su nombre"
              bind:value={formData.name}
              on:input={handleChange}
            />
          </div>
          <div class="form-group">
            <label for="email">Correo Electrónico</label>
            <input
              type="email"
              class="form-control"
              id="email"
              name="email"
              placeholder="Ingrese su correo electrónico"
              bind:value={formData.email}
              on:input={handleChange}
            />
          </div>
          <div class="form-group">
            <label for="message">Mensaje</label>
            <textarea
              class="form-control"
              id="message"
              name="message"
              rows="4"
              placeholder="Ingrese su mensaje"
              bind:value={formData.message}
              on:input={handleChange}
            ></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Enviar</button>
        </form>
      </div>
      <div class="col-md-6">
        <img src="https://media.istockphoto.com/id/530685719/es/foto/grupo-de-empresarios-de-pie-en-el-pasillo-sonriendo-y-hablando-juntos.jpg?s=2048x2048&w=is&k=20&c=FdTif-9QmtB-CnShFXphbfzvMkCRZ7UHfODI1Jr32Cw=" alt="Figura" class="img-fluid" />
      </div>
    </div>    
  </div>
</div>