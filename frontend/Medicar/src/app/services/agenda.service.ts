import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Agenda } from '../models/Agenda';

@Injectable({
  providedIn: 'root'
})
export class AgendaService {
  baseUrl = environment.apiURL + 'agendas/'

  constructor(private http: HttpClient) {

  }

  getAgendas() : Observable<Agenda[]> {
    return this.http.get<Agenda[]>(this.baseUrl);
  }
}
