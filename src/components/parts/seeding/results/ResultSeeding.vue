<template>
  <div class="data-res-view">
    <div ref="canvasRow" id="rezult">
      <div class="res-ogorod">
        <div class="row">
          <div>Расстояние между рядов:</div>
          <div>
            {{ distanceBetweenRows }} см ( {{ distanceBetweenRows / 100 }} м )
          </div>
        </div>
        <div class="row">
          <div>Растояние между кустов:</div>
          <div>
            {{ distanceBetweenBushes }} см ( {{ distanceBetweenBushes / 100 }} м
            )
          </div>
        </div>
        <div class="row">
          <div>Ширина грядки:</div>
          <div>{{ width }} см ( {{ width / 100 }} м )</div>
        </div>
        <div class="row">
          <div>Длина грядки:</div>
          <div>{{ height }} см ( {{ height / 100 }} м )</div>
        </div>
        <div class="row">
          <div>Перимитр:</div>
          <div>{{ (2 * (width + height)) / 100 }} м</div>
        </div>
        <div class="row">
          <div>Площадь:</div>
          <div>
            {{ ((width / 100) * (height / 100)).toFixed(1) }} кв. м (
            {{ ((width / 100) * (height / 100) * 0.01).toFixed(1) }}
            соток )
          </div>
        </div>
        <div class="row">
          <div>В одном ряду:</div>
          <div>{{ oneRows }} кустов</div>
        </div>
      </div>
    </div>

    <ModalWindow :show="saveResultBtn">
      <FleshMesseges dop="lite" :messages="errorSaveForm" />
      <InputForm
        typeInput="text"
        idLabel="nameSeeding"
        :modelValue="nameSeeding"
        @update:modelValue="(e) => (nameSeeding = e)"
        placeholder="Введите название грядки"
      />
      <BrnGroup>
        <ButtonExp class="btn-modal" @click="seedingSave">Сохранить</ButtonExp>
        <ButtonExp
          class="btn-outline close btn-modal"
          @click="saveResultBtn = !saveResultBtn"
        >
          Отмена
        </ButtonExp>
      </BrnGroup>
    </ModalWindow>

    <BrnGroup>
      <ButtonExp
        class="btn-outline btn-mini"
        @click="saveResultBtn = !saveResultBtn"
      >
        Сохранить результат </ButtonExp
      ><ButtonExp class="btn-outline btn-mini">
        Запланировать посадку
      </ButtonExp>
    </BrnGroup>

    <div class="picture" v-show="width !== 0 && height !== 0">
      <h3>Схема грядки</h3>
      <BrnGroup>
        <ButtonExp
          @click.prevent="zoomAction()"
          class="btn-outline btn-modal-mini btn-yellow"
        >
          -
        </ButtonExp>
        <ButtonExp
          @click.prevent="zoomAction(true)"
          class="btn-outline btn-modal-mini btn-yellow"
        >
          +
        </ButtonExp>
      </BrnGroup>
      <canvas ref="canvas" id="canvas"></canvas>
    </div>
  </div>
</template>

<script>
import ButtonExp from "@/components/ui/ButtonExp.vue";
import BrnGroup from "@/components/ui/Button/BrnGroup.vue";
import resultMixin from "../mixins/resultMixin";
import InputForm from "@/components/ui/form/InputForm.vue";
import ModalWindow from "@/components/ui/ModalWindow.vue";
import FleshMesseges from "@/components/ui/FleshMesseges.vue";
export default {
  name: "ResultSeeding",
  mixins: [resultMixin],
  data() {
    return {
      oneRows: null, // Кустов в одном ряду
      width: null, // Ширина грядки
      height: null, // Длина грядки
      saveResultBtn: false,
      nameSeeding: "",
      saveStatus: false,
      errorSaveForm: [],
    };
  },
  watch: {
    active() {
      this.run();
      //console.log(newValue);
    },
  },
  props: {
    active: { type: Number, default: 1 },
    bushes: {
      type: [String, Number],
    },
    rows: {
      type: [String, Number],
    },
    distanceBetweenRows: {
      type: [String, Number],
    },
    distanceBetweenBushes: {
      type: [String, Number],
    },
  },
  mounted() {
    this.run();
  },
  updated() {},
  methods: {
    seedingSave() {
      this.errorSaveForm =
        this.nameSeeding === "" || !this.nameSeeding
          ? ["Поле обязательно к заполнению"]
          : [];
    },
    run() {
      this.resultShow();
      this.canvasRef(this.$refs.canvas, this.$refs.canvasRow);
    },
    zoomAction(minus = false) {
      if (minus === true) {
        this.zoom = this.zoom - 0.2 < 0 ? 0.1 : this.zoom - 0.2;
      } else {
        this.zoom = this.zoom + 0.2 > 3 ? 3 : this.zoom + 0.2;
      }
      this.canvasRef(this.$refs.canvas, this.$refs.canvasRow);
    },
  },
  components: {
    ButtonExp,
    BrnGroup,
    InputForm,
    ModalWindow,
    FleshMesseges,
  },
};
</script>

<style lang="scss" scoped>
.data-res-view {
  width: 100%;
  position: relative;
}

.grup {
  width: 100%;
}

.res-ogorod {
  .row {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #a0a0a021;
  }
}
.picture {
  overflow: overlay;
  max-width: 960px;
  padding: 40px;
  text-align: center;
}

.res-ogorod {
  border-top: 1px solid #ccccccba;
  padding: 20px 80px;
  @include screen-size(sm) {
    padding: 10px 0px;
  }
  margin-top: 20px;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
  font-size: 13rem;
  font-weight: 600;
  font-style: italic;

  .res-group {
    border-bottom: 1px solid #0b0b0b0d;
    display: flex;
    justify-content: space-between;
  }
}

.picture {
  h3 {
    text-align: center;
    padding-bottom: 20px;
  }
}

.btn-save {
  display: flex;
  justify-content: center;
  gap: 5px;
  padding: 4px;
  border-radius: 3px;
  background-color: rgb(255, 255, 255);
  width: auto;
  margin: 0 auto;
  box-shadow: 0 0 3px rgb(0, 0, 0);
}
</style>
