import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CriarContaComponent } from './components/criar-conta/criar-conta.component';
import { LoginComponent } from './components/login/login.component';

const routes: Routes = [
  { path: "login", component: LoginComponent },
  { path:"criar-conta", component: CriarContaComponent,},
  { path: "", redirectTo:"login", pathMatch: "full" },
  { path: "**", redirectTo:"login", pathMatch: "full" },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
