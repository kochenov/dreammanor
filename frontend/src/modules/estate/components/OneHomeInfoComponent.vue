<template>
  <q-bar class="q-mb-md q-px-none bg-white text-black">
    <q-rating
      :model-value="3"
      max="5"
      size="24px"
      color="yellow"
      icon="star_border"
      icon-selected="star"
      icon-half="star_half"
      no-dimming
    />

    <q-space />
    <div class="q-pr-xl gt-sm">
      <q-chip
        v-if="item && item.region"
        square
        icon="travel_explore"
        size="11px"
        >{{ item.region.label }}
      </q-chip>
      <q-chip
        v-if="item && item.district"
        square
        icon="o_directions"
        size="11px"
        >{{ item.district.label }}
      </q-chip>
      <q-chip v-if="item && item.settlement" square icon="map" size="11px"
        >{{ item.settlement.settlement_type.label }}
      </q-chip>
      <q-chip
        v-if="item && item.settlement"
        square
        icon="o_holiday_village"
        size="11px"
        >{{ item.settlement.label }}
      </q-chip>
    </div>
    <q-chip size="11px" square>
      <q-avatar color="grey-8" icon="o_visibility" text-color="white" />
      <span class="q-px-sm">{{ item.views_count }}</span>
    </q-chip>

    <q-icon
      name="favorite_border"
      size="24px"
      class="custom-btn cursor-pointer"
    />

    <q-btn
      class="q-pl-sm"
      v-if="authStore.user && authStore.user.is_active"
      dense
      size="14px"
      color="grey"
      flat
      icon="list"
    >
      <q-menu auto-close>
        <q-list dense style="min-width: 100px">
          <q-item clickable>
            <q-item-section>Cut</q-item-section>
          </q-item>
          <q-item clickable>
            <q-item-section>Copy</q-item-section>
          </q-item>
          <q-item clickable>
            <q-item-section>Paste</q-item-section>
          </q-item>
          <q-separator />
          <q-item clickable>
            <q-item-section>Select All</q-item-section>
          </q-item>
        </q-list>
      </q-menu>
    </q-btn>
  </q-bar>
  <div class="row q-col-gutter-md" v-if="item">
    <div class="col-12 col-md-6">
      <q-card>
        <q-item v-if="!item.video_zen">
          <q-item-section avatar>
            <q-avatar color="primary" text-color="white" icon="o_videocam" />
          </q-item-section>

          <q-item-section>
            <q-item-label>Видео обзор дома в деревне</q-item-label>
            <q-item-label caption>{{ item.meta_title }}</q-item-label>
          </q-item-section>
        </q-item>
        <div class="q-video">
          <q-responsive :ratio="16 / 9">
            <iframe
              v-if="!item.video_zen"
              :src="`https://dzen.ru/embed/${item.video_zen}?from_block=partner&from=zen&backoffice=1&mute=1&autoplay=0&tv=0`"
              allow="autoplay; fullscreen; accelerometer; gyroscope; picture-in-picture; encrypted-media"
              frameborder="0"
              scrolling="no"
              allowfullscreen=""
            ></iframe>
            <q-img
              :src="`https://api.dreammanor.ru/${item.main_image}`"
              :ratio="16 / 9"
            />
          </q-responsive>
        </div>
      </q-card>
      <div class="column q-my-sm">
        <q-btn
          dense
          color="primary"
          label="Обзор дома"
          icon="o_smart_display"
        />
      </div>
    </div>
    <div class="column col-sm-12 col-md-6">
      <q-card class="my-card q-pa-sm">
        <q-list>
          <q-item clickable v-ripple active-class="bg-teal-1 text-grey-8">
            <q-item-section avatar>
              <q-icon color="green" name="o_payments" />
            </q-item-section>
            <q-item-section>Цена</q-item-section>
            <q-item-section side
              ><span class="text-h5">{{ currentPrice }} </span>
            </q-item-section>
          </q-item>
          <q-separator spaced inset />
          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="primary" name="o_cottage" />
            </q-item-section>

            <q-item-section>
              <q-item-label>Площадь дома</q-item-label>
              <q-item-label caption>Обычно это общая площадь дома</q-item-label>
            </q-item-section>
            <q-item-section side top>
              <q-badge color="primary" :label="item.area_of_house" />
              <span>кв.м</span>
            </q-item-section>
          </q-item>

          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="red" name="fence" />
            </q-item-section>

            <q-item-section>
              <q-item-label>Размер участка</q-item-label>
              <q-item-label caption>1 сотка = 100 кв.м</q-item-label>
            </q-item-section>
            <q-item-section side top>
              <q-badge color="secondary" :label="item.plot_area" />
              <span> соток</span>
            </q-item-section>
          </q-item>
          <q-separator spaced inset />
          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="blue" name="o_water_drop" />
            </q-item-section>

            <q-item-section>
              <q-item-label>Вода</q-item-label>
              <q-item-label caption>Водоснабжение</q-item-label>
            </q-item-section>
            <q-item-section side top>
              <q-item-label caption>{{
                item.bathroom_in_house ? "в доме" : "колодец"
              }}</q-item-label>
              <q-icon
                :name="item.bathroom_in_house ? 'o_check_circle' : 'o_cancel'"
                :color="item.bathroom_in_house ? 'green' : 'red'"
              />
            </q-item-section>
          </q-item>

          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="orange" name="o_propane_tank" />
            </q-item-section>

            <q-item-section>
              <q-item-label>Газ</q-item-label>
              <q-item-label caption>Снабжение газом</q-item-label>
            </q-item-section>
            <q-item-section side top>
              <q-item-label caption>{{
                item.bathroom_in_house ? "газ есть" : "газа нет"
              }}</q-item-label>
              <q-icon
                :name="item.bathroom_in_house ? 'o_check_circle' : 'o_cancel'"
                :color="item.bathroom_in_house ? 'green' : 'red'"
              />
            </q-item-section>
          </q-item>

          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="green" name="o_bathtub" />
            </q-item-section>

            <q-item-section>
              <q-item-label>Санитарный узел</q-item-label>
              <q-item-label caption>Туалет, ванна, душ</q-item-label>
            </q-item-section>
            <q-item-section side top>
              <q-item-label caption>{{
                item.bathroom_in_house ? "в доме" : "на участке"
              }}</q-item-label>
              <q-icon
                :name="item.bathroom_in_house ? 'o_check_circle' : 'o_cancel'"
                :color="item.bathroom_in_house ? 'green' : 'red'"
              />
            </q-item-section>
          </q-item>
          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="info" name="o_explore" />
            </q-item-section>

            <q-item-section>
              <q-item-label>Полный адрес дома</q-item-label>
              <q-item-label caption>{{ item.full_adress }}</q-item-label>
            </q-item-section>
            <q-item-section side>
              <q-icon name="pin_drop" color="green" />
            </q-item-section>
          </q-item>
        </q-list>
      </q-card>

      <div class="q-mt-md">
        <div class="row q-gutter-sm">
          <q-btn
            class="col-md-4 col-12"
            dense
            outline
            color="red-10"
            label="Оставить отзыв"
            icon="o_add_comment"
          />

          <q-btn
            class="col-md col-12"
            dense
            outline
            color="primary"
            label="Дзен"
            icon="rss_feed"
          />
          <q-btn
            dense
            outline
            @click="confirm_to_avito = !confirm_to_avito"
            push
            class="col-md col-12"
            color="primary"
            label="Задать вопрос"
            icon="help_outline"
          />
        </div>
      </div>
      <q-dialog v-model="confirm_to_avito" persistent>
        <q-card class="q-pa-sm">
          <q-card-section class="row items-center justify-center">
            <span class="text-subtitle2">
              Связаться с хозяином дома можно только на сайте Авито!
            </span>
            <span class="text-subtitle2">
              Подтвердите переход на страницу объявления.
            </span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn label="Отмена" flat color="red" v-close-popup />
            <q-btn
              label="Перейти"
              :href="`${item.link_to_ads}`"
              target="_blank"
              color="secondary"
              outline
              v-close-popup
            />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>

    <div class="col-md-6 col-12"></div>
    <div class="col-md-6 col-12 text-body1">
      <h2 class="q-my-sm q-mx-xs text-h6">
        Описание дома в {{ item.settlement.settlement_type.label_i }}
        {{ item.settlement.label_i }}
      </h2>
      <div class="q-px-sm" v-html="item.description"></div>
    </div>
  </div>
  <div v-else>Объявления отсутствуют</div>
 </template>

<script setup>
import { useAuthStore } from "src/stores/all";
import { computed, ref } from "vue";

const authStore = useAuthStore();
const props = defineProps(["item"]);
const confirm_to_avito = ref(false);


const currentPrice = computed(() => {
  return props.item.price.toLocaleString("ru-RU", {
    style: "currency",
    currency: "RUB",
    minimumFractionDigits: 0,
  });
});
</script>

<style lang="scss" scoped>
.custom-btn {
  color: grey;
  &:hover {
    color: red;
  }
}
</style>
