import { Agenda } from "./Agenda";
import { Medico } from "./Medico";

export class Consulta {
  id!: number;
  medico!: Medico;
  dia!: Date;
  agenda!: Agenda;
  horario: any;
}
