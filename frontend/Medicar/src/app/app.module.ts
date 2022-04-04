import { AgendaService } from './services/agenda.service';
import { MedicoService } from './services/medico.service';
import { EspecialidadeService } from './services/especialidade.service';
import { HomeComponent } from './components/home/home.component';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { ToastrModule } from 'ngx-toastr';
import { ModalModule } from 'ngx-bootstrap/modal';

import { AccountService } from 'src/app/services/account.service';

import { JwtInterceptor } from './interceptors/jwt.interceptor';

import { AppComponent } from './app.component';
import { CriarContaComponent } from './components/criar-conta/criar-conta.component';
import { ButtonsComponent } from './shared/buttons/buttons.component';
import { LoginComponent } from './components/login/login.component';
import { MarcarConsultaComponent } from './components/marcar-consulta/marcar-consulta.component';
import { ConsultaService } from './services/consulta.service';



@NgModule({
  declarations: [
    AppComponent,
    CriarContaComponent,
    ButtonsComponent,
    LoginComponent,
    HomeComponent,
    MarcarConsultaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    ToastrModule.forRoot(),
    HttpClientModule,
    ModalModule.forRoot(),
  ],
  providers: [
    ConsultaService,
    AccountService,
    EspecialidadeService,
    AgendaService,
    MedicoService,
    {provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
