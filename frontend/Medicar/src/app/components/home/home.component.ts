

import { Component, OnInit, TemplateRef } from '@angular/core';
import { Router } from '@angular/router';
import { AccountService } from 'src/app/services/account.service';
import { Consulta } from 'src/app/models/Consulta';
import { BsModalRef, BsModalService } from 'ngx-bootstrap/modal';
import { ConsultaService } from 'src/app/services/consulta.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  modalRef: BsModalRef | any;
  consultaId = 0;
  message?: string;
  consultas: Consulta[] = [];
  showModal?: boolean;

  constructor(public accountService: AccountService,
              private router: Router,
              private consultaService: ConsultaService,
              private modalService: BsModalService,
              private toastr: ToastrService) { }

  ngOnInit(): void {
    this.getConsultas();

  }

  getConsultas():void{
    this.consultaService.getConsultas().subscribe({
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

  openModalMarcarConsulta() {
    this.showModal = true;
  }

  closeModal() {
    this.showModal = false;
  }



  decline(): void {
    this.message = 'Declined!';
    this.modalRef?.hide();
  }


  openModal(event: any, template: TemplateRef<any>, consultaId: number): void {
    event.stopPropagation();
    this.consultaId = consultaId;
    this.modalRef = this.modalService.show(template, { class: 'modal-sm' });
  }

  confirm(): void {
    this.modalRef.hide();

    this.consultaService
      .deleteConsulta(this.consultaId)
      .subscribe(
        (result: any) =>
            window.location.replace('/home'),
        (error: any) => {
          console.error(error);
          this.toastr.error(
            `Erro ao tentar deletar a consulta ${this.consultaId}`,
            'Erro'
          );
        }
      )
  }

}
