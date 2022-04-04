import { ConsultaService } from 'src/app/services/consulta.service';
import { AgendaService } from './../../services/agenda.service';
import { MedicoService } from './../../services/medico.service';
import { Especialidade } from './../../models/Especialidade';
import { Component, OnInit, NgModule, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { EspecialidadeService } from 'src/app/services/especialidade.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Medico } from 'src/app/models/Medico';
import { Agenda } from 'src/app/models/Agenda';
import { Location } from '@angular/common';
import { Consulta } from 'src/app/models/Consulta';
import { AccountService } from 'src/app/services/account.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-marcar-consulta',
  templateUrl: './marcar-consulta.component.html',
  styleUrls: ['./marcar-consulta.component.scss']
})
export class MarcarConsultaComponent implements OnInit {
  form!: FormGroup;
  especialidadeId!: number;
  agendaId!: number;
  medicoName!: number;
  hora_is_true!: boolean;

  horario: any[] = [];
  agendasData: any = [];
  medicosNomes: any = [];
  especialidades: Especialidade[] = [];
  medicos: Medico[] = [];
  agendas: Agenda[] = [];

  consulta= {} as Consulta;

  @Output()
  closeEvent = new EventEmitter();


  constructor(private especialidadeService: EspecialidadeService,
              private activatedRouter: ActivatedRoute,
              private medicoService: MedicoService,
              private agendaService: AgendaService,
              public fb: FormBuilder,
              private _location:Location,
              private consultaService: ConsultaService,
              private router: Router,
              private toaster: ToastrService,
              ) { }

  ngOnInit(): void {

    this.getEspecialidades();
    this.getMedicos();
    this.filtraMedico();
    this.getAgendas();
    this.validation();
  }


  private validation():void {


    this.form = this.fb.group({
      especialidade: ['', Validators.required],
      medico: ['', Validators.required],
      agenda: ['', Validators.required],
      horario: ['', Validators.required],
    });
  }

  getEspecialidades():void{
    let especialidades_:any;
    this.especialidadeService.getEspecialidades().subscribe({
      next:(especialidades: Especialidade[]) => {
        this.especialidades = especialidades;
        especialidades_ = especialidades;
        let especialidadesJson: any = JSON.stringify(especialidades_);
        localStorage.setItem("especialidades",especialidadesJson);
      },
      error:(error: any) => console.log(error)
    });
  }

  getMedicos():void{
    let medicos_:any;
    this.medicoService.getMedicos().subscribe({
      next:(medicos: Medico[]) => {
        this.medicos = medicos;
        medicos_ = medicos;
        let medicosJson: any = JSON.stringify(medicos_);
        localStorage.setItem("medicos",medicosJson);
      },
      error:(error: any) => console.log(error)
    });
  }

  getAgendas():void{
    let agendas_:any;
    this.agendaService.getAgendas().subscribe({
      next:(agendas: Agenda[]) => {
        this.agendas = agendas;
        agendas_ = agendas;
        let agendasJson: any = JSON.stringify(agendas_);
        localStorage.setItem("agendas",agendasJson);
      },
      error:(error: any) => console.log(error)
    });
  }

  filtraMedico(){
    let especialidades : any = localStorage.getItem("especialidades");
    especialidades = JSON.parse(especialidades);
    localStorage.removeItem("especialidades");




  }

  onChangeMedicos():boolean{
    let active:boolean = false;
    while(this.medicosNomes.length) {
      this.medicosNomes.pop();
      this.agendasData.pop();
    }


    this.especialidadeId = this.form.controls["especialidade"].value;

    let medicos : any = localStorage.getItem("medicos");
    medicos = JSON.parse(medicos);

    for (var medico of medicos) {
      if(this.especialidadeId === medico.especialidade.id){
        this.medicosNomes.push(medico.nome);
        active =true;
      }
    }
      return active

  }


  onChangeData(){
    let active:boolean = false;

    while(this.agendasData.length) {
      this.agendasData.pop();
      // this.horario.pop();
    }

    this.medicoName = this.form.controls["medico"].value;

    let agendas : any = localStorage.getItem("agendas");
    agendas = JSON.parse(agendas);

    for (var agenda of agendas) {
      if(this.medicoName === agenda.medico.nome){
        this.agendasData.push(agenda.dia);
        active =true;
      }
    }

    return active
  }

  onChangeHora() {

    let agendaData: any;
    agendaData = this.form.controls["agenda"].value;

    let agendas_ : any = localStorage.getItem("agendas");
    agendas_ = JSON.parse(agendas_);

    for (var agenda of agendas_) {
      if(agendaData === agenda.dia){
        this.agendaId = agenda.id;
        this.horario = agenda.horario;
        this.hora_is_true =true;
      }
    }
    return this.hora_is_true;
  }


  register():void {
    this.form.controls["agenda"].setValue(this.agendaId);
    this.consulta = { ...this.form.value};

    this.consultaService.post(this.consulta).subscribe(
      () => window.location.replace('/home'),
      (error: any) => this.toaster.error(error.error)
    )
  }

  hideModal(action: boolean = false) {
    this.closeEvent.emit(action)
  }

}
