import { Especialidade } from './../models/Especialidade';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class EspecialidadeService {

  baseUrl = environment.apiURL + 'especialidades/'

  constructor(private http: HttpClient) {

  }

  getEspecialidades() : Observable<Especialidade[]> {
    return this.http.get<Especialidade[]>(this.baseUrl);
  }
}
