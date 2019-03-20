<template>
  <div id="app">
    <div id="header-nav" class="nav-bars">
      <div class="nav-design">
        <router-link to="/">Home</router-link>|
        <router-link to="/uploads">Uploads</router-link>|
        <router-link to="/recommender">Recommender</router-link>
      </div>
    </div>
    <div class="router-wrap">
      <router-view />
    </div>
    <div id="footer-nav" class="nav-bars">READ Toolkit</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      uploadCount: 0
    };
  }
};
</script>

<style lang="scss">
body {
  overflow: hidden;
  margin: 0;
}
h1,
h2,
h3,
h4,
h5,
h6,
a,
p,
span {
  margin: 0;
}

.router-wrap {
  margin: 50px 0px;
  height: 90vh;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  .nav-bars {
    background: cornflowerblue;
    display: flex;
    position: fixed;
    height: 5vh;
    align-items: center;
    justify-content: center;
    width: 100%;
    color: white;

    .nav-design {
      width: 40%;
      height: 100%;
      align-items: center;
      display: flex;
      justify-content: space-around;
    }

    a {
      color: white;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100%;
      text-decoration: none;
    }
    a:hover {
      background-color: white;
      color: cornflowerblue;
      cursor: pointer;
    }
  }

  #header-nav {
    top: 0;
    left: 0;
  }

  #footer-nav {
    bottom: 0;
    left: 0;
  }
}
</style>
