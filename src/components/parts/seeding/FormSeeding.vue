<template>
  <div class="calc-seeding">
    <FleshMesseges :messages="messages" />
    <FleshMesseges
      v-if="errorDataApi"
      :messages="[
        'Не удалось получить данные с сервера! Проверьте интернет соединение...',
      ]"
    />
    <FormGrid>
      <RowInput>
        <SelectForm
          :modelValue="currentSort"
          @update:modelValue="(e) => loadDataSorts(e)"
          :options="sorts"
          :name="'Выберите сорт овоща, ' + vegetable.name"
          idLabel="sort"
        >
          <SelectOptionForm selected disabled value="default"
            >Сорт не выбран</SelectOptionForm
          >
        </SelectForm>

        <InputForm
          typeInput="number"
          min="1"
          max="1000"
          placeholder="Введите положительное число от 1 до 1000"
          name="Количество кустов"
          idLabel="bushes"
          :modelValue="bushes"
          @update:modelValue="(e) => (bushes = e)"
        />
        <InputForm
          typeInput="number"
          min="1"
          max="500"
          placeholder="Введите положительное число от 1 до 500"
          name="Количество рядов"
          idLabel="rows"
          :modelValue="rows"
          @update:modelValue="(e) => (rows = e)"
        />
      </RowInput>
      <RowInput>
        <InputForm
          typeInput="number"
          min="1"
          max="500"
          placeholder="Введите положительное число от 1 до 500"
          name="Расстояние между рядов, см"
          idLabel="distanceBetweenRows"
          :modelValue="distanceBetweenRows"
          @update:modelValue="(e) => (distanceBetweenRows = e)"
        />
        <InputForm
          typeInput="number"
          min="1"
          max="500"
          placeholder="Введите положительное число от 1 до 500"
          name="Расстояние между кустов, см"
          idLabel="distanceBetweenBushes"
          :modelValue="distanceBetweenBushes"
          @update:modelValue="(e) => (distanceBetweenBushes = e)"
        />
      </RowInput>
      <BrnGroup>
        <ButtonExp @click.prevent="submitToResult"> Сделать расчёт </ButtonExp>
      </BrnGroup>
    </FormGrid>
  </div>
</template>

<script>
import FleshMesseges from "@/components/ui/FleshMesseges.vue";
import FormGrid from "../../ui/form/FormGrid.vue";
import RowInput from "@/components/ui/form/RowInput.vue";
import InputForm from "@/components/ui/form/InputForm.vue";
import SelectForm from "@/components/ui/form/SelectForm.vue";
import SelectOptionForm from "@/components/ui/form/SelectOptionForm.vue";
import ButtonExp from "@/components/ui/ButtonExp.vue";
import BrnGroup from "../../ui/Button/BrnGroup.vue";
import { mapState, mapGetters } from "vuex";

export default {
  name: "FormSeeding",
  data() {
    return {
      messages: [],
      loadingDataApi: true,
      currentSort: "default",
      distanceBetweenRows: "",
      distanceBetweenBushes: "",
      bushes: "1",
      rows: "1",
    };
  },

  computed: {
    ...mapState({
      errorDataApi: (state) => state.errorDataApi,
    }),
    ...mapGetters({
      sorts: "getSorts",
      vegetable: "getVegetable",
    }),
  },
  methods: {
    loadDataSorts(id) {
      this.currentSort = id;
      let sort = this.sorts.find((item) => item.id == id);
      this.distanceBetweenRows = sort.distanceBetweenRows;
      this.distanceBetweenBushes = sort.distanceBetweenBushes;
    },

    submitToResult() {
      // Если все поля формы заполнены
      if (
        this.distanceBetweenRows !== "" &&
        this.distanceBetweenBushes !== "" &&
        this.bushes !== "" &&
        this.rows !== ""
      ) {
        if (this.bushes >= this.rows) {
          // Если кнопка не была ранее нажата
          if (!this.result) {
            // меняем состояние на нажатое
            this.result = true;
            // Очищаем список ошибок
            this.message = "";
          }
          // Количество кустов в одном ряду
          this.oneRows = Math.ceil(this.bushes / this.rows);
          // Ширины грядки
          this.width =
            this.rows * this.distanceBetweenRows + this.distanceBetweenRows;
          // Длины грядки
          this.height =
            this.oneRows * this.distanceBetweenBushes +
            this.distanceBetweenBushes;
          let сanvasEl = this.$refs.canvas;
          сanvasEl.setAttribute("width", Math.ceil(this.height / 2));
          // Растягиваем полотно по высоте
          сanvasEl.setAttribute("height", Math.ceil(this.width / 2));
          let canvas = сanvasEl.getContext("2d");
          // Рисуем прямоугольник
          canvas.strokeRect(
            0,
            0,
            Math.ceil(this.height / 2),
            Math.ceil(this.width / 2)
          );
          this.canvasRow(canvas);
          setTimeout(() => {
            this.$refs.canvasRow.scrollIntoView({
              block: "start",
              behavior: "smooth",
            });
          }, 1);
        } else {
          // Если не все поля заполнены выводим сообщение
          this.message = [
            "Количество рядов не должно превышать количество кустов!",
          ];
          // Меняем состояние
          this.result = false;
        }
      } else {
        // Если не все поля заполнены выводим сообщение
        this.message = ["Пожалуйста, заполните все поля формы!"];
        // Меняем состояние
        this.result = false;
      }
    },
  },
  components: {
    FleshMesseges,
    FormGrid,
    RowInput,
    InputForm,
    SelectForm,
    SelectOptionForm,
    ButtonExp,
    BrnGroup,
  },
};
</script>

<style lang="scss" scoped></style>
