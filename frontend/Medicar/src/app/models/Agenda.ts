import { Medico } from "./Medico";

export class Agenda {
  id!: number;
  medico!: Medico;
  dia!: Date;
  horarios: any;
}
