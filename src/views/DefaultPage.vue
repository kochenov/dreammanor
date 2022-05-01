<template>
  <div class="wrap">
    <div style="padding: 60px">
      <h2>Сайт находится на стадии глубокой разработки</h2>
      <p>Просим протестировать страницу расчёта размера грядок</p>
      <div class="wr-link">
        <router-link to="/calculation/seeding"> Расчёт грядок</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DefaultPage",
  data: () => ({}),
};
</script>
<style lang="scss" scoped>
h2 {
  text-align: center;
  padding: 40px;
}
p {
  text-align: center;
  padding: 10px;
  font-weight: 600;
}
.wr-link {
  display: flex;
  justify-content: center;
  padding: 10px;
  a {
    margin: 0 auto;
    text-align: center;
    text-decoration: none;
    color: #194484;
    border: 2px solid #194484;
    border-radius: 4px;
    padding: 10px 40px;
    &:hover {
      color: #ffffff;
      border: 2px solid #194484;
      background: #194484;
    }
  }
}
</style>
