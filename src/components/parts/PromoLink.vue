<template>
  <div class="promo-info-link">
    <button @click="discrement" class="promo-info-link__btn-left">
      <fa icon="angle-left" />
    </button>
    <ul class="promo-info-link__items">
      <li class="promo-info-link__item">
        <a class="promo-info-link__link" :href="links[num].url">
          {{ links[num].textLink }}
          <span class="color"> {{ links[num].textLinkOn }}</span></a
        >
      </li>
    </ul>
    <button @click="increment" class="promo-info-link__btn-right">
      <fa icon="angle-right" />
    </button>
  </div>
</template>

<script>
export default {
  name: "PromoLink",
  data() {
    return {
      num: 0,
      links: [
        { url: "/", textLink: "TEST", textLinkOn: "Подпишитесь на Ютуб Канал" },
        {
          url: "/calculation/seeding",
          textLink: "Весна близко!",
          textLinkOn: " Планируй свой огород!",
        },
      ],
    };
  },
  methods: {
    increment() {
      if (this.links.length - 1 === this.num) {
        this.num = 0;
      } else {
        ++this.num;
      }
    },
    discrement() {
      if (this.num === 0) {
        this.num = this.links.length - 1;
      } else {
        --this.num;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
$promo-info-link-color1: rgb(245, 250, 255);
.promo-info-link {
  height: 34px;
  background-color: #17696a;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
  ul {
    list-style: none;
    padding: 0 5px;
  }
  a {
    text-decoration: none;
    color: $promo-info-link-color1;
    font-size: 13px;
    span {
      padding-left: 4px;
    }
    &:hover {
      color: #b6fafb;
    }
  }
  button {
    background: none;
    border: none;
    color: $promo-info-link-color1;
    font-size: 9px;
    cursor: pointer;
    padding: 5px;
  }
}

.color {
  color: #fff700;
}
</style>
