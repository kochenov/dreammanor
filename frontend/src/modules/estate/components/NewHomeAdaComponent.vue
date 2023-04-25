<template>
  <div class="row flex-center">
    <div class="col-12">
      <q-form>
        <q-stepper v-model="step" vertical color="primary" animated>
          <q-step
            :name="1"
            title="Место расположения дома"
            icon="settings"
            caption="Указать регион, район и название поселения, улицу и дом"
            :done="step > 1"
          >
            <!--Карточка в списке-->

            <!-- Адрес -->
            <div class="row q-mt-sm wrap q-col-gutter-md">
              <q-select
                :key="modal_form_add_region"
                class="col-12 col-sm"
                v-model="form_data.region"
                filled
                use-input
                input-debounce="0"
                label="Выбрать регион"
                :options="region_id_options"
                @update:modelValue="loadDistrict()"
                @filter="region_id_filter_fn"
                behavior="dialog"
                :loading="load_regions_status"
              >
                <template v-slot:no-option>
                  <q-item>
                    <q-item-section class="text-grey">
                      Список регионов пуст. Добавьте новый регион
                    </q-item-section>
                  </q-item>
                </template>
                <template v-slot:append>
                  <q-btn
                    round
                    dense
                    flat
                    icon="add"
                    @click.stop.prevent="modal_form_add_region = true"
                  />
                </template>
                <q-dialog
                  v-model="modal_form_add_region"
                  persistent
                  transition-show="flip-down"
                  transition-hide="flip-up"
                >
                  <q-card style="width: 300px">
                    <q-card-section>
                      <div class="text-h6">Добавить новый регион</div>
                    </q-card-section>

                    <q-card-section class="q-pt-none">
                      <q-input
                        v-model="new_region"
                        label="Введите название региона"
                        dense
                        error-message="Такой регион уже есть"
                      />
                    </q-card-section>

                    <q-card-actions align="right" class="bg-white text-teal">
                      <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
                      <q-btn
                        flat
                        label="ДОБАВИТЬ"
                        @click="save_new_region_to_base"
                      />
                    </q-card-actions>
                  </q-card>
                </q-dialog>
              </q-select>

              <q-select
                :key="modal_form_add_district"
                class="col-12 col-sm"
                v-model="form_data.district"
                filled
                :disable="!form_data.region && load_regions_status"
                :error="!form_data.region"
                error-message="Выбирите сначала регион"
                use-input
                input-debounce="0"
                label="Выбрать район"
                :options="district_id_options"
                @update:modelValue="loadSettlementTypes()"
                @filter="district_id_filter_fn"
                behavior="dialog"
                :loading="load_districts_status"
              >
                <template v-slot:no-option>
                  <q-item>
                    <q-item-section class="text-grey">
                      Список районов пуст. Добавьте новый район
                    </q-item-section>
                  </q-item>
                </template>
                <template v-slot:append>
                  <q-btn
                    round
                    dense
                    flat
                    icon="add"
                    @click.stop.prevent="modal_form_add_district = true"
                  />
                </template>
                <q-dialog
                  v-if="form_data.region"
                  v-model="modal_form_add_district"
                  persistent
                  transition-show="flip-down"
                  transition-hide="flip-up"
                >
                  <q-card style="width: 300px">
                    <q-card-section>
                      <div class="text-h6">Добавить новый район</div>
                    </q-card-section>

                    <q-card-section class="q-pt-none">
                      <q-input
                        v-model="new_district"
                        label="Введите название региона"
                        dense
                        error-message="Такой регион уже есть"
                      />
                    </q-card-section>

                    <q-card-actions align="right" class="bg-white text-teal">
                      <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
                      <q-btn
                        flat
                        label="ДОБАВИТЬ"
                        @click="save_new_district_to_base"
                      />
                    </q-card-actions>
                  </q-card>
                </q-dialog>
              </q-select>

              <q-select
                :key="modal_form_add_settlement_type"
                class="col-12 col-sm"
                v-model="form_data.settlement_type"
                filled
                use-input
                input-debounce="0"
                label="Выбрать тип поселения"
                :options="settlement_type_id_options"
                @update:modelValue="loadSettlements"
                @filter="settlement_type_id_filter_fn"
                behavior="dialog"
                :loading="load_settlement_types_status"
                :disable="!form_data.region || !form_data.district"
                :error="!form_data.region || !form_data.district"
                error-message="Выбирите сначала регион и район"
              >
                <template v-slot:no-option>
                  <q-item>
                    <q-item-section class="text-grey">
                      Список типов поселений пуст. Добавьте новый тип
                    </q-item-section>
                  </q-item>
                </template>
                <template v-slot:append>
                  <q-btn
                    round
                    dense
                    flat
                    icon="add"
                    @click.stop.prevent="modal_form_add_settlement_type = true"
                  />
                </template>
                <q-dialog
                  v-model="modal_form_add_settlement_type"
                  persistent
                  transition-show="flip-down"
                  transition-hide="flip-up"
                >
                  <q-card style="width: 300px">
                    <q-card-section>
                      <div class="text-h6">Добавить тип поселения</div>
                    </q-card-section>

                    <q-card-section class="q-pt-none">
                      <q-input
                        v-model="new_settlement_type"
                        label="Введите название типа поселения"
                        dense
                        error-message="Такой тип уже есть"
                      />
                      <q-input
                        class="q-pt-md"
                        v-model="new_settlement_type_i"
                        label="Как будет на вопрос где?"
                        dense
                        error-message="Такой тип уже есть"
                      />
                    </q-card-section>

                    <q-card-actions align="right" class="bg-white text-teal">
                      <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
                      <q-btn
                        flat
                        label="ДОБАВИТЬ"
                        @click="save_new_settlement_type_to_base"
                      />
                    </q-card-actions>
                  </q-card>
                </q-dialog>
              </q-select>

              <q-select
                @blur="updateFullAdress"
                :key="modal_form_add_settlement"
                class="col-12 col-sm"
                v-model="form_data.settlement"
                filled
                :disable="
                  !form_data.region ||
                  !form_data.district ||
                  !form_data.settlement_type
                "
                :error="
                  !form_data.region ||
                  !form_data.district ||
                  !form_data.settlement_type
                "
                error-message="Выбирите сначала регион, район и тип поселения"
                use-input
                input-debounce="0"
                label="Выбрать поселение"
                :options="settlement_id_options"
                @focus="loadSettlements()"
                @filter="settlement_id_filter_fn"
                behavior="dialog"
                :loading="load_settlements_status"
              >
                <template v-slot:no-option>
                  <q-item>
                    <q-item-section class="text-grey">
                      Список поселений пуст. Добавьте новое поселение
                    </q-item-section>
                  </q-item>
                </template>
                <template v-slot:append>
                  <q-btn
                    round
                    dense
                    flat
                    icon="add"
                    @click.stop.prevent="modal_form_add_settlement = true"
                  />
                </template>
                <q-dialog
                  v-if="form_data.region && form_data.district"
                  v-model="modal_form_add_settlement"
                  persistent
                  transition-show="flip-down"
                  transition-hide="flip-up"
                >
                  <q-card style="width: 300px">
                    <q-card-section>
                      <div class="text-h6">Добавить поселение</div>
                    </q-card-section>

                    <q-card-section class="q-pt-none">
                      <q-input
                        v-model="new_settlement"
                        label="Введите название поселения"
                        dense
                        error-message="Такое поселение уже есть"
                      />
                      <q-input
                        class="q-pt-md"
                        v-model="new_settlement_i"
                        label="Как будет на вопрос Где?"
                        dense
                        error-message="Такое поселение уже есть"
                      />
                    </q-card-section>

                    <q-card-actions align="right" class="bg-white text-teal">
                      <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
                      <q-btn
                        flat
                        label="ДОБАВИТЬ"
                        @click="save_new_settlement_to_base"
                      />
                    </q-card-actions>
                  </q-card>
                </q-dialog>
              </q-select>
            </div>

            <q-separator color="orange q-my-lg" inset />

            <!-- Полный адрес -->
            <q-input
              class="q-my-md"
              filled
              autocomplete="Off"
              v-model="form_data.full_adress"
              label="Полный адрес *"
              hint="Полный адрес в формате: Регион, район, село, улица, № дома"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Заполнять обязательно',
              ]"
            />

            <q-stepper-navigation>
              <q-btn
                @click="
                  form_data.full_adress &&
                  form_data.region &&
                  form_data.district &&
                  form_data.settlement_type &&
                  form_data.settlement
                    ? (step = 2)
                    : Inform()
                "
                color="primary"
                label="Продолжить"
              />
            </q-stepper-navigation>
          </q-step>

          <q-step
            :name="2"
            title="Основные характеристики дома"
            caption="Ввести площадь дома, площадь участка, цену на дом, наличие комуникаций"
            icon="create_new_folder"
            :done="step > 2"
          >
            <div class="row q-mt-sm wrap q-col-gutter-md">
              <!-- Цена дома -->
              <q-input
                class="col-12 col-sm"
                filled
                v-model="form_data.price"
                label="Цена дома"
                type="number"
                :min="1"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- Площадь дома -->
              <q-input
                class="col-12 col-sm"
                filled
                type="number"
                v-model="form_data.area_of_house"
                label="Площадь дома"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- Площадь участка  -->
              <q-input
                class="col-12 col-sm"
                filled
                type="number"
                v-model="form_data.plot_area"
                label="Площадь участок"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
            </div>
            <!-- Характеристики дополнительные -->
            <q-toggle
              v-model="form_data.bathroom_in_house"
              label="Туалет дома"
              color="green"
              checked-icon="check"
              unchecked-icon="clear"
            />
            <!-- Газ -->
            <q-toggle
              v-model="form_data.gaz"
              label="Газ"
              color="green"
              checked-icon="check"
              unchecked-icon="clear"
            />

            <q-separator color="orange q-mt-lg" inset />

            <h6>Количество комнат</h6>
            <!-- количество комнат -->
            <div class="q-gutter-sm">
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="1"
                label="1 комната"
              />
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="2"
                label="2 комнаты"
              />
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="3"
                label="3 комнаты"
              />
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="4"
                label="4 комнаты"
              />
              <q-radio
                v-model="form_data.number_of_rooms"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="5"
                label="5 комнат"
              />
            </div>

            <h6>Количество этажей</h6>
            <!-- количество этажей -->
            <div class="q-gutter-sm">
              <q-radio
                v-model="form_data.number_of_floors"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="1"
                label="1 этаж"
              />
              <q-radio
                v-model="form_data.number_of_floors"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="2"
                label="2 этажа"
              />
              <q-radio
                v-model="form_data.number_of_floors"
                checked-icon="task_alt"
                unchecked-icon="panorama_fish_eye"
                val="3"
                label="3 этажа"
              />
            </div>

            <h6>Дополнительные параметры объявления</h6>
            <!-- количество этажей -->
            <div class="column q-gutter-sm q-mb-md">
              <!-- Пластиковые окна -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.plastic_windows"
                label="Пластиковые окна"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Характеристики основные  -->
              <!-- Наличие бани -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.sauna"
                label="Баня"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- автобусная остановка -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.bus_stop"
                label="Наличие автобусной остановки"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие ж/д станции -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.rail_station"
                label="Наличие ж/д остановки"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие рядом леса -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.there_is_a_forest_nearby"
                label="Наличие рядом леса"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие газового отопления -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.gas_heating"
                label="Наличие газового отопления"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие печного отопления -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.furnace_heating"
                label="Наличие печного отопления"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Наличие канализации -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.sewerage"
                label="Наличие канализации"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />

              <!-- Аварийный дом -->
              <q-toggle
                class="col-12 col-sm"
                v-model="form_data.alarm_status"
                label="Аварийное состояние дома"
                color="green"
                checked-icon="check"
                unchecked-icon="clear"
              />
            </div>
            <div class="row q-mt-sm wrap q-col-gutter-md">
              <!-- Расстояние до реки -->
              <q-input
                class="col-12 col-sm"
                filled
                v-model="form_data.distance_to_the_river"
                label="Расстояние до реки"
                type="number"
                :min="1"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- Расстояние до озера -->
              <q-input
                class="col-12 col-sm"
                filled
                v-model="form_data.distance_to_the_lake"
                label="Расстояние до озера"
                type="number"
                :min="1"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- Расстояние до города -->
              <q-input
                class="col-12 col-sm"
                filled
                v-model="form_data.distance_to_the_city"
                label="Расстояние до города"
                type="number"
                :min="1"
                lazy-rules
                :rules="[
                  (val) => (val && val > 0) || 'Число должно быть больше нуля',
                ]"
              />
              <!-- год постройки -->
              <q-input
                class="col-12 col-sm"
                filled
                hint="Год: XXXX"
                v-model="form_data.year_of_construction"
                label="Год постройки"
                type="number"
                :min="1901"
                :max="curr_yaer"
                lazy-rules
                :rules="[
                  (val) =>
                    (val > 1900 && val <= curr_yaer) ||
                    'Число должно быть больше 1900 и не больше ' + curr_yaer,
                ]"
              />

              <!-- Материал стен -->
              <q-input
                class="col-12 col-sm"
                fille
                v-model="form_data.wall_material_id"
                label="Материал стен"
                type="number"
              />
            </div>
            <q-stepper-navigation>
              <q-btn
                @click="
                  form_data.plot_area &&
                  form_data.price &&
                  form_data.area_of_house
                    ? (step = 3)
                    : Inform()
                "
                color="primary"
                label="Продолжить"
              />
              <q-btn
                flat
                @click="step = 1"
                color="primary"
                label="Назад"
                class="q-ml-sm"
              />
            </q-stepper-navigation>
          </q-step>

          <q-step
            :name="3"
            title="Видео обзоры"
            caption="Ссылки на объявление и видео ролик "
            icon="create_new_folder"
            :done="step > 3"
          >
            <!-- Ссылка на объявление -->
            <q-input
              class="q-my-md"
              type="url"
              aria-required
              filled
              v-model="form_data.link_to_ads"
              label="Ссылка на объявление"
              hint="Ссылка на объявление для автоматической переадресации"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Заполнять обязательно',
              ]"
            />
            <!-- Видео Дзен -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.video_zen"
              label="Видео рилик из Dzen"
              hint="Ввести код"
              lazy-rules
            />
            <!-- Видео Рутуб -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.video_rutube"
              label="Видео рилик из Рутуб"
              hint="Ввести код"
              lazy-rules
            />

            <q-stepper-navigation>
              <q-btn
                @click="
                  form_data.full_adress &&
                  form_data.link_to_ads &&
                  (form_data.video_zen || form_data.video_rutube)
                    ? (step = 4)
                    : Inform()
                "
                color="primary"
                label="Продолжить"
              />
              <q-btn
                flat
                @click="step = 2"
                color="primary"
                label="Назад"
                class="q-ml-sm"
              />
            </q-stepper-navigation>
          </q-step>

          <q-step
            :name="4"
            title="Название и описание"
            caption="Написать описание к объявлению и видео обзору"
            icon="create_new_folder"
            :done="step > 4"
          >
            <!-- Заголовок -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.title"
              label="Заголовок объявления *"
              hint="Для привлечения внимания"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length < 200) ||
                  'Заголовок обязателен для заполнения',
              ]"
            />
            <!-- Мета Заголовок -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.meta_title"
              label="Заголовок Meta-Title *"
              hint="Для SEO"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length < 200) ||
                  'Заголовок обязателен для заполнения',
              ]"
            />
            <!-- Описание -->
            <q-editor
              v-model="form_data.description"
              @blur="textClean()"
              paragraph-tag="p"
              :toolbar="[['bold', 'italic']]"
              min-height="5rem"
            />
            <!--  <q-input
              class="q-my-md"
              filled
              v-model="form_data.description"
              type="textarea"
              label="Описание к объявлению *"
              hint="Показывается на странице объявления"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Заполнять обязательно',
              ]"
            /> -->
            <!-- Описание -->
            <q-input
              class="q-my-md"
              filled
              v-model="form_data.meta_description"
              type="textarea"
              label="Мета Описание *"
              hint="SEO"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length < 500) ||
                  'Заголовок обязателен для заполнения',
              ]"
            />

            <q-stepper-navigation>
              <q-btn
                @click="
                  form_data.title && form_data.description
                    ? (step = 5)
                    : Inform()
                "
                color="primary"
                label="Продолжить"
              />
              <q-btn
                flat
                @click="step = 3"
                color="primary"
                label="Назад"
                class="q-ml-sm"
              />
            </q-stepper-navigation>
          </q-step>

          <q-step :name="5" title="Публикация материала" icon="add_comment">
            <!---->
            <q-uploader
              @added="initImage"
              :auto-upload="false"
              :multiple="false"
              accept=".jpg, .jpeg, .png"
              hide-upload-btn
              label="Картинка карточки"
            />
            <!--UID-->
            <div class="row">
              <q-input
                class="q-my-md col-md-3 col-sm-12"
                filled
                v-model="form_data.uid"
                type="number"
                label="Уникальный код *"
                hint="Код по которому можно найти объявление"
                lazy-rules
                :rules="[
                  (val) =>
                    (val && val.length > 0) || 'Обязателен для заполнения',
                ]"
              />
            </div>

            <!-- Вкл черновик -->
            <q-toggle
              v-model="form_data.status"
              label="Опубликовать объявление"
              color="green"
              checked-icon="check"
              unchecked-icon="clear"
            />
            <q-stepper-navigation>
              <q-btn color="primary" @click="onSubmit" label="Публиковать" />
              <q-btn
                flat
                @click="step = 4"
                color="primary"
                label="Назад"
                class="q-ml-sm"
              />
            </q-stepper-navigation>
          </q-step>
        </q-stepper>
      </q-form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, computed } from "vue";
import axios from "axios";
import { useEstateStore } from "../store";
import { Notify } from "quasar";
import DOMPurify from "dompurify";
const estateStore = useEstateStore();

const step = ref(1);
const image = ref(null);

const curr_yaer = computed(() => {
  const now = new Date();
  const currentYear = now.getFullYear();
  return currentYear;
});
// форм
const form_data = ref({
  title: "",
  description: "",
  meta_title: "",
  meta_description: "",
  status: false,
  region: null,
  district: null,
  settlement_type: null,
  settlement: null,
  full_adress: null,
  main_image: null,
  video_zen: null,
  video_rutube: null,
  link_to_ads: null,
  price: null,
  area_of_house: null,
  plot_area: null,
  bathroom_in_house: false,
  gaz: false,
  uid: null,
  //
  number_of_rooms: null,
  number_of_floors: null,
  sauna: false,
  plastic_windows: false,
  bus_stop: false,
  rail_station: false,
  distance_to_the_river: null,
  distance_to_the_lake: null,
  there_is_a_forest_nearby: false,
  distance_to_the_city: null,
  gas_heating: false,
  furnace_heating: false,
  sewerage: false,
  year_of_construction: null,
  wall_material_id: null,
  alarm_status: false,
});
onMounted(() => {
  loadRegions();
});
/*********  Адрес ****************************/
/* Регион */
// Добавление нового региона
const modal_form_add_region = ref(false);
const new_region = ref(null);

const save_new_region_to_base = async () => {
  if (new_region.value) {
    await estateStore.addNewRegion({ label: new_region.value });
    new_region.value = null;
    if (!estateStore.error) {
      loadRegions();
      modal_form_add_region.value = false;
    }
  }
};
// Отображение списка, филтрация и выбор региона
const region_id_string_options = ref(null);
const region_id_options = ref(region_id_string_options.value);
const region_id_filter_fn = (val, update) => {
  if (val === "") {
    update(() => {
      region_id_options.value = region_id_string_options.value;
    });
    return;
  }

  update(() => {
    const needle = val.toLowerCase();
    region_id_options.value = region_id_string_options.value.filter(
      (v) => v.label.toLowerCase().indexOf(needle) > -1
    );
  });
};

/* Район региона */
// Добавление нового Района
const modal_form_add_district = ref(false);
const new_district = ref(null);

const save_new_district_to_base = async () => {
  if (new_district.value) {
    await estateStore.addNewDistrict({
      label: new_district.value,
      region_id: form_data.value.region.id,
    });
    new_district.value = null;
    if (!estateStore.error) {
      loadDistrict();
      modal_form_add_district.value = false;
    }
  }
};

const district_id_string_options = ref([]);
const district_id_options = ref(district_id_string_options.value);
const district_id_filter_fn = (val, update) => {
  if (val === "") {
    update(() => {
      district_id_options.value = district_id_string_options.value;
    });
    return;
  }

  update(() => {
    const needle = val.toLowerCase();
    district_id_options.value = district_id_string_options.value.filter(
      (v) => v.label.toLowerCase().indexOf(needle) > -1
    );
  });
};

//*** Типы поселений *****************************/
const modal_form_add_settlement_type = ref(false);
const new_settlement_type = ref(null);
const new_settlement_type_i = ref(null);

const save_new_settlement_type_to_base = async () => {
  if (new_settlement_type.value) {
    await estateStore.addNewSettlementType({
      label: new_settlement_type.value,
      label_i: new_settlement_type_i.value,
    });
    new_settlement_type.value = null;
    new_settlement_type_i.value = null;
    if (!estateStore.error) {
      loadSettlementTypes();
      modal_form_add_settlement_type.value = false;
    }
  }
};

const settlement_type_id_string_options = ref(null);
const settlement_type_id_options = ref(settlement_type_id_string_options.value);
const settlement_type_id_filter_fn = (val, update) => {
  if (val === "") {
    update(() => {
      settlement_type_id_options.value =
        settlement_type_id_string_options.value;
    });
    return;
  }

  update(() => {
    const needle = val.toLowerCase();
    settlement_type_id_options.value =
      settlement_type_id_string_options.value.filter(
        (v) => v.label.toLowerCase().indexOf(needle) > -1
      );
  });
};

/* Поселение *************************************/
// Добавление нового Поcеления
const modal_form_add_settlement = ref(false);
const new_settlement = ref(null);
const new_settlement_i = ref(null);

const save_new_settlement_to_base = async () => {
  if (new_settlement.value && new_settlement_i.value) {
    await estateStore.addNewSettlement({
      label: new_settlement.value,
      label_i: new_settlement.value,
      region_id: form_data.value.region.id,
      district_id: form_data.value.district.id,
      settlement_types_id: form_data.value.settlement_type.id,
    });
    new_settlement.value = null;
    new_settlement_i.value = null;
    if (!estateStore.error) {
      loadSettlements();
      modal_form_add_settlement.value = false;
    }
  }
};

const settlement_id_string_options = ref(null);
const settlement_id_options = ref(settlement_id_string_options.value);
const settlement_id_filter_fn = (val, update) => {
  if (val === "") {
    update(() => {
      settlement_id_options.value = settlement_id_string_options.value;
    });
    return;
  }

  update(() => {
    const needle = val.toLowerCase();
    settlement_id_options.value = settlement_id_string_options.value.filter(
      (v) => v.label.toLowerCase().indexOf(needle) > -1
    );
  });
};
/*********  End Поселение Адрес *********/

/***** Upload Image*****/

const uploadImage = async () => {
  try {
    const response = await axios.post(
      "https://api.dreammanor.ru/realty/upload-images/",
      image.value,
      {
        headers: {
          Accept: "application/json",
          "Content-Type": "multipart/form-data",
        },
      }
    );
    form_data.value.main_image = response.data[0].url;
  } catch (error) {
    console.error(error);
  }
};

const initImage = (file) => {
  const formData = new FormData();
  formData.append("images", file[0]);
  image.value = formData;
};

/***** End Upload Image*****/

/** Загрузка и обновление регионов */
const load_regions_status = ref(false);
const loadRegions = async () => {
  load_regions_status.value = true;
  //--
  form_data.value.district = null;
  form_data.value.settlement_type = null;
  form_data.value.settlement = null;
  //--
  await estateStore.getRegions();
  region_id_string_options.value = estateStore.regions;
  if (region_id_string_options.value) {
    setTimeout(() => {
      load_regions_status.value = false;
    }, 60);
  }
};

/** Загрузка и обновление районов */
const load_districts_status = ref(false);
const loadDistrict = async () => {
  load_districts_status.value = true;
  if (form_data.value.region) {
    let region = form_data.value.region.id;
    //--
    form_data.value.settlement_type = null;
    form_data.value.settlement = null;
    //--
    await estateStore.getDistricts(region);
    district_id_string_options.value = estateStore.districts;
    setTimeout(() => {
      load_districts_status.value = false;
    }, 60);
  } else {
    Notify.create({
      message: "Для выбора района, сначала нужно выбрать регион",
      color: "red",
    });
  }
};

/** Загрузка и обновление типов поселений */
const load_settlement_types_status = ref(false);
const loadSettlementTypes = async () => {
  //--
  form_data.value.settlement = null;
  //--
  await estateStore.getSettlementTypes();
  settlement_type_id_string_options.value = estateStore.settlement_types;
};

/** Загрузка и обновление поселений */
const load_settlements_status = ref(false);
const loadSettlements = async () => {
  if (
    form_data.value.region &&
    form_data.value.district &&
    form_data.value.settlement_type
  ) {
    let region = form_data.value.region.id;
    let district = form_data.value.district.id;
    let settlement_type = form_data.value.settlement_type.id;
    await estateStore.getSettlements(region, district, settlement_type);
    settlement_id_string_options.value = estateStore.settlements;
  } else {
    Notify.create({
      message: "Для выбора поселения, сначала нужно выбрать регион и район",
      color: "red",
    });
  }
};

/********** Установка адреса ***********/
const updateFullAdress = () => {
  if (
    form_data.value.region &&
    form_data.value.district &&
    form_data.value.settlement_type &&
    form_data.value.settlement
  ) {
    form_data.value.full_adress = `${form_data.value.region.label}, ${form_data.value.district.label}, ${form_data.value.settlement_type.label} ${form_data.value.settlement.label}`;
  }
};

const onSubmit = async () => {
  await uploadImage();
  if (form_data.value.main_image) {
    let data = {
      title: form_data.value.title,
      description: form_data.value.description,
      meta_title: form_data.value.meta_title,
      meta_description: form_data.value.meta_description,
      status: form_data.value.status,
      region_id: form_data.value.region.id,
      district_id: form_data.value.district.id,
      settlement_id: form_data.value.settlement.id,
      full_adress: form_data.value.full_adress,
      main_image: form_data.value.main_image,
      video_zen: form_data.value.video_zen,
      video_rutube: form_data.value.video_rutube,
      link_to_ads: form_data.value.link_to_ads,
      price: form_data.value.price,
      area_of_house: form_data.value.area_of_house,
      plot_area: form_data.value.plot_area,
      bathroom_in_house: form_data.value.bathroom_in_house,
      gaz: form_data.value.gaz,
      uid: form_data.value.uid,
    };
   await estateStore.addNewHome(data);
    if (!estateStore.error) {
      form_data.value = {
        title: null,
        description: null,
        meta_title: null,
        meta_description: null,
        status: false,
        region_id: null,
        district_id: null,
        settlement_id: null,
        full_adress: null,
        main_image: null,
        video_zen: null,
        video_rutube: null,
        link_to_ads: null,
        price: null,
        area_of_house: null,
        plot_area: null,
        bathroom_in_house: false,
        gaz: false,
        uid: null,
      };
      step.value = 1;
    }
  } else {
    Notify.create({
      message: "Для перехода к следующему шагу заполните все поля формы",
      color: "red",
    });
  }
};

const Inform = () => {
  Notify.create({
    message: "Для перехода к следующему шагу заполните все поля формы",
    color: "red",
  });
};

const textClean = () => {
  form_data.value.description = DOMPurify.sanitize(
    form_data.value.description,
    { ALLOWED_TAGS: ["b", "p", "i"], ALLOWED_ATTR: ["accesskey"] }
  );
  console.log(form_data.value.description);
};
</script>

<style lang="scss" scoped></style>
