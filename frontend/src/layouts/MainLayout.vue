<template>
  <q-layout view="lhh Lpr lfr">
    <q-ajax-bar position="top" color="red" size="4px" />
    <q-header class="color-bg text-white" height-hint="69">
      <q-toolbar>
        <q-btn
          dense
          flat
          round
          icon="menu"
          class="text-primary"
          @click="toggleLeftDrawer"
        />
        <div class="flex flex-center lt-md" style="width: 100%">
          <h6
            class="text-subtitle2 text-black cursor-pointer q-ma-none"
            @click.prevent="toggleRightDrawer"
          >
            МЕНЮ
          </h6>
        </div>
        <TopMenu
          @subMenu="
            (e) => {
              tab = e;
            }
          "
        />

        <q-space />

        <q-btn
          v-if="authStore.user && authStore.user.id && authStore.user.is_superuser == true"
          color="primary"
          outline
          dense
          flat
          square
          fab-mini
          icon="note_add"
          class="q-mr-xs"
        >
          <q-menu>
            <q-list dense style="min-width: 100px">
              <q-item
                clickable
                @click="newsStore.open_add_news = true"
                v-close-popup
              >
                <q-item-section>Новость</q-item-section>
              </q-item>
              <q-item clickable v-close-popup>
                <q-item-section>Категорию к новости</q-item-section>
              </q-item>
              <q-separator />
              <q-item clickable to="/desk/realEstate/links/add-new-ads-home">
                <q-item-section>Объявление</q-item-section>
              </q-item>
              <q-separator />
              <q-item clickable v-close-popup>
                <q-item-section>Админка</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>
        <q-btn
          v-if="!authStore.user"
          color="primary"
          outline
          dense
          flat
          square
          fab-mini
          icon="login"
        >
          <q-menu>
            <div class="row no-wrap q-pa-lg">
              <div class="column">
                <div class="text-h6 q-mb-md">Авторизация</div>
                <q-btn
                  color="primary"
                  label="Вход"
                  push
                  square
                  icon="login"
                  to="/login"
                  size="sm"
                  class="q-ma-xs q-px-xs"
                  v-close-popup
                />
                <q-btn
                  color="primary"
                  label="Регистрация"
                  push
                  outline
                  square
                  to="/registration"
                  size="sm"
                  icon="person_add"
                  class="q-ma-xs q-px-xs shadow-0"
                  v-close-popup
                />
              </div>

              <q-separator vertical inset class="q-mx-lg" />

              <div class="column justify-center items-center">
                <q-avatar
                  size="72px"
                  color="primary"
                  text-color="white"
                  icon="admin_panel_settings"
                />
              </div>
            </div>
          </q-menu>
        </q-btn>
        <q-btn
          v-if="authStore.user"
          color="primary"
          outline
          dense
          flat
          square
          fab-mini
          icon="account_circle"
        >
          <q-menu>
            <div class="row no-wrap q-pa-md">
              <div class="column">
                <div class="text-h6 q-mb-md">Аккаунт</div>
                <q-btn
                  color="primary"
                  label="Профиль"
                  outline
                  push
                  size="sm"
                  class="q-mt-sm"
                  v-close-popup
                />
                <q-btn
                  color="primary"
                  outline
                  label="Кабинет"
                  push
                  size="sm"
                  class="q-mt-sm"
                  v-close-popup
                />
              </div>

              <q-separator vertical inset class="q-mx-lg" />

              <div class="column items-center">
                <q-avatar size="72px" color="secondary" icon="person">
                </q-avatar>

                <div class="text-subtitle1 q-mt-md q-mb-xs">
                  {{ authStore.user.username }}
                </div>

                <q-btn
                  color="primary"
                  label="Выход"
                  push
                  to="/logout"
                  size="sm"
                  v-close-popup
                />
              </div>
            </div>
          </q-menu>
        </q-btn>
      </q-toolbar>

      <SubMenu :tabName="tab" />
      <HeaderPromo />
      <BreadcrumbsHeader v-if="$route.name != 'home'" />
    </q-header>

    <q-drawer v-model="leftDrawerOpen" bordered>
      <LeftPart />
    </q-drawer>
    <q-drawer
      v-model="rightDrawerOpen"
      bordered
      side="right"
      behavior="mobile"
      overlay
    >
      <q-list separator padding class="text-primary">
        <q-item v-ripple>
          <q-item-section avatar>
            <q-icon
              class="pointer"
              @click="subMenuMobail = null"
              v-if="subMenuMobail != null"
              name="keyboard_backspace"
            />
          </q-item-section>

          <q-item-section
            ><span
              class="pointer"
              @click="subMenuMobail = null"
              v-if="subMenuMobail != null"
              >Назад</span
            ></q-item-section
          >

          <q-separator vertical inset="item-thumbnail" />
          <q-item-section class="pointer" @click="toggleRightDrawer()" side>
            <q-icon name="close" />
          </q-item-section>
        </q-item>
        <q-separator />
        <TopMenu
          v-if="subMenuMobail == null"
          mobile
          @subMenuMobile="
            (e) => {
              subMenuMobail = e;
            }
          "
        />
        <SubMenu mobile :tab-name="subMenuMobail" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <q-page class="">
        <AddNews />
        <router-view />
      </q-page>
    </q-page-container>
    <q-footer elevated class="bg-grey-10 text-white">
      <q-toolbar class="flex flex-center">
        Усадьба Мечты &copy; 2023
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { useAuthStore, useNewsStore } from "src/stores/all";

import { ref } from "vue";
import TopMenu from "../components/navs/menu/TopMenu.vue";
import SubMenu from "../components/navs/menu/SubMenu.vue";
import HeaderPromo from "../components/promo/HeaderPromo.vue";
import BreadcrumbsHeader from "../components/navs/BreadcrumbsHeader.vue";
import LeftPart from "../components/parts/LeftPart.vue";
import { defineAsyncComponent } from "vue";

const AddNews = defineAsyncComponent(() =>
  import("src/modules/news/components/admin/newPost.vue")
);

const leftDrawerOpen = ref(false);
const rightDrawerOpen = ref(false);
const authStore = useAuthStore();
const newsStore = useNewsStore();
const tab = ref("home");
const subMenuMobail = ref(null);

const toggleLeftDrawer = () => {
  leftDrawerOpen.value = !leftDrawerOpen.value;
};
const toggleRightDrawer = () => {
  rightDrawerOpen.value = !rightDrawerOpen.value;
  subMenuMobail.value = null;
};
</script>
<style lang="scss">
.my-menu-link {
  color: white;
  background: #f2c037;
}
.pointer {
  cursor: pointer;
}
</style>
