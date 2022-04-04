import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Medico } from '../models/Medico';

@Injectable({
  providedIn: 'root'
})
export class MedicoService {
  baseUrl = environment.apiURL + 'medicos/'

  constructor(private http: HttpClient) {

  }

  getMedicos() : Observable<Medico[]> {
    return this.http.get<Medico[]>(this.baseUrl);
  }
}
