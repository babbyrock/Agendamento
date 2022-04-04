import { AuthGuard } from './guard/auth.guard';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CriarContaComponent } from './components/criar-conta/criar-conta.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';

const routes: Routes = [
  { path: "", redirectTo:"login", pathMatch: "full" },
  { path: "login", component: LoginComponent },
  { path:"criar-conta", component: CriarContaComponent,},

  { path: '',
    runGuardsAndResolvers: 'always',
    canActivate: [AuthGuard],
    children:[
      { path:"home", component: HomeComponent,},
    ],
    },

  { path: "**", redirectTo:"login", pathMatch: "full" },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
