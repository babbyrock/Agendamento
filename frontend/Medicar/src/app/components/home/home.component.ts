import { ConsultaService } from './../../services/Consultas/consulta.service';

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AccountService } from 'src/app/services/Account/account.service';
import { Consulta } from 'src/app/models/Consulta';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  consultas: Consulta[] = [];

  constructor(public accountService: AccountService,
              private router: Router,
              private consutaService: ConsultaService) { }

  ngOnInit(): void {+
    this.getConsultas();

  }

  getConsultas():void{
    this.consutaService.getConsultas().subscribe({
      next:(consultas: Consulta[]) => {
        this.consultas = consultas;
      },
      error:(error: any) => console.log(error)
    });

  }


  logout(): void {
    this.accountService.logout();
    window.location.replace('/login');
  }
}
